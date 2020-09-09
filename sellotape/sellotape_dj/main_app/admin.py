from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
class User(models.Model):
	# Inherits Attributes from User default instance
    user 	= models.OneToOneField(User, on_delete=models.CASCADE)
    # Generates a user ID which is the primary identifier to the user
    user_id	= models.AutoField(primary_key=True)
    # User avatar, optional: limit the image instance height and width
    avatar	= models.ImageField()
    country	= models.CharField(default='Israel')
    
	class city(models.TextChoices):
	     	tel_aviv 	= 'ta', _('Tel Aviv')
	     	hamerkaz 	= 'me', _('HaMerkaz')
	     	hadarom 	= 'da', _('HaDarom')
	     	hatzafon 	= 'tz', _('HaTzafon')
    city	= models.CharField(
        max_length=2,
        choices=city.choices,
        default=city.hamerkaz,
    ) 		 

    