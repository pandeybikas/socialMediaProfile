from django.contrib import admin
from .models import Profile,Post, Comment, Likes, Reply, FollowerCount
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(Reply)
admin.site.register(FollowerCount)