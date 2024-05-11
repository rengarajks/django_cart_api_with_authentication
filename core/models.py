from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email=models.CharField(unique=True,max_length=120)
