from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})