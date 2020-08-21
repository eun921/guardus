from django.db import models
import accounts.models

class Post(models.Model):
    author=models.ForeignKey(accounts.models.User, related_name='mypost_set',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    address=models.CharField(max_length=100)
    image=models.ImageField(upload_to="%Y/%m/%d")
    tag_set=models.ManyToManyField('Tag')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author=models.ForeignKey(accounts.models.User, on_delete=models.CASCADE)
    post=models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE, blank=True)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name=models.CharField(max_length=20, unique=True)
    icon=models.ImageField(upload_to="posting/icon")