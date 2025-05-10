from django.contrib.auth.models import *
from django.db import models
from django.conf import settings
from django.utils import timezone

class CustomUser(AbstractUser):
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='images/avatar.png', blank=True)
    business_name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.email})"