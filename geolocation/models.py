from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
