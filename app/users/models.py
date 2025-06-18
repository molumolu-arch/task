from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    coins = models.PositiveIntegerField(default=0)
    REQUIRED_FIELDS = ['email']

   