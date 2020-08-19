from django.conf import settings
from django.db import models

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    warning=models.PositiveIntegerField(default=0)