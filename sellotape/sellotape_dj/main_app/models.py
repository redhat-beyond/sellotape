from django.db import models


class user_followers(models.Model):
    user_followers_id 	=     user_id = models.AutoField(primary_key=True)
    user_id 			= models.ForeignKey('self', on_delete=models.CASCADE)
    follower_id 		= models.ForeignKey(User, on_delete=models.CASCADE)