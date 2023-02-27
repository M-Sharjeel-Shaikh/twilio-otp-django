from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
