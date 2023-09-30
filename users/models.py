from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # pass

    # Para crear un superusuario comentar esta parte
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


