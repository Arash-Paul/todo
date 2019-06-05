from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class UserModel(AbstractBaseUser):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=255, unique=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
