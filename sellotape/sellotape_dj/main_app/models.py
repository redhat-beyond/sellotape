from django.db import models
from django.contrib.auth.models import User

# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
class Profile(models.Model):
    # Inherits Attributes from User default instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # User avatar, optional: limit the image instance height and width
    avatar = models.ImageField()
    country = models.CharField(max_length=100, default='Israel')
    youtube_link = models.URLField(max_length=200, null=True)
    twitch_link = models.URLField(max_length=200, null=True)
    
    class City(models.IntegerChoices):
        tel_aviv = '1', 'Tel Aviv'
        hamerkaz = '2', 'HaMerkaz'
        hadarom = '3', 'HaDarom'
        hatzafon = '4', 'HaTzafon'
    
    city = models.IntegerField(
        choices=City.choices,
        default=City.tel_aviv,
    )   

class UserFollowers(models.Model):
    user_followers_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('self', on_delete=models.CASCADE)
    follower_id	= models.ForeignKey(Profile, on_delete=models.CASCADE)

class Stream(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    link = models.URLField(max_length=500, blank=False)
    description = models.TextField(max_length=50, null=True)
    airs_on = models.DateField()
    ends_on = models.DateField(null=True)
    added_on = models.DateField()

    class Meta:
        ordering = ['airs_on', 'author']
        db_table = 'streams'
