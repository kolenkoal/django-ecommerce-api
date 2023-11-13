from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient


class DjoserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "phone_number": "+79261234567",
            "email": "jane.smith@example.com",
            "password": "S3cur3P@ss",
            # "re_password": "S3cur3P@ss"
        }

        self.user = get_user_model().objects.create_user(**self.user_data)
        self.user.is_active = True
        self.user.save()

    def test_user_registration(self):
        user_data = {
            "first_name": "James",
            "last_name": "Smith",
            "phone_number": "+79261254567",
            "email": "james.smith@example.com",
            "password": "S3cur3P@ss",
            "re_password": "S3cur3P@ss",
        }
        # Validate password confirmation
        response = self.client.post("/auth/users/", user_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["email"], user_data["email"])
        self.assertEqual(response.data["first_name"], user_data["first_name"])
        self.assertEqual(response.data["last_name"], user_data["last_name"])
        self.assertEqual(
            response.data["phone_number"], user_data["phone_number"]
        )

        self.assertNotIn("password", response.data)

    def test_user_login(self):
        data = {
            "email": self.user_data["email"],
            "password": self.user_data["password"],
        }
        response = self.client.post("/auth/jwt/create/", data)
        self.assertEqual(
            response.status_code, 200
        )  # 200 OK for successful login
        self.assertTrue("access" in response.data)
        self.assertTrue("refresh" in response.data)

    def test_user_profile(self):
        user_data_copy = self.user_data.copy()
        if "re_password" in user_data_copy:
            del user_data_copy["re_password"]

        self.client.force_authenticate(user=self.user)
        response = self.client.get("/auth/users/me/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data["email"], self.user_data["email"])
        self.assertEqual(
            response.data["first_name"], self.user_data["first_name"]
        )
        self.assertEqual(
            response.data["last_name"], self.user_data["last_name"]
        )
        self.assertEqual(
            response.data["phone_number"], self.user_data["phone_number"]
        )
