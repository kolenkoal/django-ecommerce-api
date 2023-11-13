from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.user_data = {
            "email": "testuser@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "+1234567890",
            "password": "testpassword",
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_creation(self):
        self.assertEqual(self.user.email, self.user_data["email"])
        self.assertEqual(self.user.first_name, self.user_data["first_name"])
        self.assertEqual(self.user.last_name, self.user_data["last_name"])
        self.assertEqual(
            self.user.phone_number, self.user_data["phone_number"]
        )

    def test_user_authentication(self):
        user = User.objects.get(email=self.user_data["email"])
        self.assertTrue(user.check_password(self.user_data["password"]))

    def test_superuser_creation(self):
        superuser = User.objects.create_superuser(
            email="admin@example.com",
            first_name="Admin",
            last_name="User",
            phone_number="+9876543210",
            password="adminpassword",
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), self.user.email)

    def test_user_manager_methods(self):
        user = User.objects.create_user(
            email="testuser2@example.com",
            first_name="Jane",
            last_name="Smith",
            phone_number="+1111111111",
            password="testpassword2",
        )
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            email="admin@example.com",
            first_name="Admin",
            last_name="User",
            phone_number="+9876543210",
            password="adminpassword",
        )

        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def tearDown(self):
        self.user.delete()
