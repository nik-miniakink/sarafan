from django.contrib.auth.models import AbstractUser
from django.db import models

from app.auth2_0.managers import CustomUserManager


class User(AbstractUser):
    """
    Модель пользователя с имейлом вместо имени пользователя, имя пользователя - пустое
    """
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
