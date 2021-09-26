from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):

    def create_user(self, username, phone, password, **extra_fields):
        """
        Create and save a User with the given phone and password.
        """
        if not phone:
            raise ValueError('The phone must be set')

        user = self.model(username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given phone and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        return self.create_user(username, phone, password, **extra_fields)


class CustomUser(AbstractUser):
    gender_list = [
        ('None', 'None'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13, unique=True)
    gender = models.CharField(choices=gender_list, max_length=6, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    forget_pass_token = models.CharField(max_length=225, blank=True, null=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
