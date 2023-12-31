from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    """User manager in the system for the User model."""

    def create_user(
        self,
        email,
        first_name,
        last_name,
        phone_number,
        password=None,
        **extra_fields
    ):
        """Creates and saves a User with the given email and password."""
        if not email:
            raise ValueError("Email must be specified.")
        if not first_name:
            raise ValueError("First name must be specified.")
        if not last_name:
            raise ValueError("Last name must be specified.")
        if not phone_number:
            raise ValueError("Phone number must be specified.")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self,
        email,
        first_name,
        last_name,
        phone_number,
        password=None,
        **extra_fields
    ):
        """Creates and saves a superuser with the given email and password."""
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    """User in the system."""

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    date_joined = models.DateField(
        verbose_name="date joined", auto_now_add=True
    )

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
