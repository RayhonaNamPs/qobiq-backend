from django.contrib.auth.models import AbstractUser
from django.db import models


class Accounts(AbstractUser):
    fullname = models.CharField(max_length=50, null=True, blank=False)
    user_type = models.CharField(max_length=10, null=True, blank=False)
    age = models.IntegerField(blank=False, null=True)
    gender = models.CharField(max_length=10, blank=False, null=True)
    phone_number = models.CharField(max_length=15, blank=False, null=True)
    bio = models.TextField(blank=True, null=True)
