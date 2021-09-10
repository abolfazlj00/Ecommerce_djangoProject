from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):

    def create_user(self, phone, password, **extra_fields):
        """
        Create and save a User with the given phone and password.
        """
        if not phone:
            raise ValueError('The phone must be set')

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given phone and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        return self.create_user(phone, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13, unique=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = CustomUserManager()

    def __str__(self):
        return self.phone