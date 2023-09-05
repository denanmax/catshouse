from django.contrib.auth.models import AbstractUser
from django.db import models

from cats.models import NULLABLE


# Create your models here.

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='номер телефон', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='Имя пользователя в Телеграм', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
