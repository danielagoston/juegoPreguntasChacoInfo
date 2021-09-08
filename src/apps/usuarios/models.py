from django.contrib.auth.models import AbstractUser

from django.db import models

class Usuario(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)