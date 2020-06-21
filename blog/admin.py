from django.contrib import admin
from .models import Post, Follower

admin.site.register(Follower)
admin.site.register(Post)

