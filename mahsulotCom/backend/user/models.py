from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    choices = [
        ('product_admin','product_admin'),
        ('super_admin','super_admin'),
    ]
    role = models.CharField(max_length = 100, choices = choices)