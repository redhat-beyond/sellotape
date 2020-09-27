from django.contrib import admin
from .models import Stream, Profile, UserFollowers


admin.site.register(Stream)
admin.site.register(Profile)
admin.site.register(UserFollowers)