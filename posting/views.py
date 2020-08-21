from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

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