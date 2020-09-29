from django.contrib import admin
from .models import Stream, Profile, UserFollower


admin.site.register(Stream)
admin.site.register(Profile)
admin.site.register(UserFollower)
