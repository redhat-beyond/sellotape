from django.db import models
from django.contrib.auth.models import User
from .admin import UserProfile

class UserFollowers(models.Model):
    user_followers_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('self', on_delete=models.CASCADE)
    follower_id	= models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Stream(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    link = models.URLField(max_length=500, blank=False)
    airs_on = models.DateField()
    ends_on = models.DateField(null=True)
    added_on = models.DateField()

    class Meta:
        ordering = ['airs_on', 'author']
        db_table = 'streams'
