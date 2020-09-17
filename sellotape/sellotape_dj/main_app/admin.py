from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

# Register your models here.

# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
class UserProfile(models.Model):
    # Inherits Attributes from User default instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # User avatar, optional: limit the image instance height and width
    avatar = models.ImageField()
    country = models.CharField(max_length=100, default='Israel')
    
    class City(models.IntegerChoices):
        tel_aviv = '1', 'Tel Aviv'
        hamerkaz = '2', 'HaMerkaz'
        hadarom = '3', 'HaDarom'
        hatzafon = '4', 'HaTzafon'
    
    city = models.IntegerField(
        choices=City.choices,
        default=City.tel_aviv,
    )   