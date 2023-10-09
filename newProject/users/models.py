from django.db import models
from django.utils import timezone


class Users(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    user_email = models.EmailField(max_length=254, unique=True)
    objects = models.Manager()
