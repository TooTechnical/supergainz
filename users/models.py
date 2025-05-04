from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)

    # New fields for customers
    full_name = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
