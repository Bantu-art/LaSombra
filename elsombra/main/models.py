from django.db import models

from django.contrib.auth.models import User

class UserProfile(model.Models):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username