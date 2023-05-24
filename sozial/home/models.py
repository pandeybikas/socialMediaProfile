from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id_user= models.IntegerField(null=True)
    full_name= models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    bio = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    pic = models.ImageField(upload_to='media')
    body = models.TextField()
    created_on = models.DateField(default=datetime.now)
    likes = models.IntegerField(default= 0)

    def __str__(self):
        return self.body
    
class Comment(models.Model):
    comment_on = models.ForeignKey(Post, on_delete=models.PROTECT, null=True, related_name='comments')
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_body = models.TextField(null=True)
    comment_date = models.DateField(default=datetime.now)

class Reply(models.Model):
    reply_on = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    reply_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    reply_body = models.CharField(max_length=500, null=True)

class Likes(models.Model):
    like_on = models.CharField(max_length=100)
    liked_by = models.CharField(max_length=100)


class FollowerCount(models.Model):
    followed_by = models.CharField(max_length=100, null=True)
    followed_to = models.CharField(max_length=100, null=True)
    