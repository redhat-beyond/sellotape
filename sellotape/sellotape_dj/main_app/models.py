from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # Inherits Attributes from User default instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # User avatar, optional: limit the image instance height and width
    avatar = models.ImageField()
    country = models.CharField(max_length=100, default='Israel')
    youtube_link = models.URLField(max_length=200, blank=True)
    twitch_link = models.URLField(max_length=200, blank=True)

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
    follow_from = models.ForeignKey(Profile, related_name='follow_from', on_delete=models.CASCADE)
    follow_to = models.ForeignKey(Profile, related_name='follow_to', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follow_from', 'follow_to')

    def clean(self):
        if self.follow_from == self.follow_to:
            raise ValueError("One Cannot follow themselves")


class Stream(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    link = models.URLField(max_length=500, blank=False)
    description = models.TextField(max_length=50, blank=True, null=True)
    airs_on = models.DateTimeField()
    ends_on = models.DateTimeField(blank=True, null=True)
    added_on = models.DateTimeField()

    class Meta:
        ordering = ['airs_on', '-added_on', 'author']
        db_table = 'streams'
