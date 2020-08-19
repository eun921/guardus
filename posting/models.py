from django.db import models
from django.conf import settings

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    address=models.CharField(max_length=100)
    image=models.ImageField()
    tag_set=models.ManyToManyField('Tag')
    comment_count=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name=models.CharField(max_length=20, unique=True)
    icon=models.ImageField(upload_to="posting/icon")