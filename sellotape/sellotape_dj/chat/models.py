from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete = models.CASCADE)
    room_name = models.CharField(max_length=20)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    @staticmethod
    def last_messages(num_of_msgs, room_name):
        return Message.objects.filter(room_name=room_name).order_by('-timestamp').all()[:num_of_msgs][::-1]
