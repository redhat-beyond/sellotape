from django.db import models
from django.contrib.auth.models import User

class Stream(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(max_length=500, blank=False)
    airs_on = models.DateField()
    ends_on = models.DateField(null=True)
    added_on = models.DateField()

    class Meta:
        ordering = ['airs_on', 'author']
        db_table = 'streams'
