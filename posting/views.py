from .models import Post, Comment
from .serializers import PostSerializer, DetailSerializer, CommentSerializer, CreateSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

class PostViewSet(ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class CommentViewSet(ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

class DetailViewSet(RetrieveAPIView):
    lookup_field='pk'
    queryset=Post.objects.all()
    serializer_class=DetailSerializer

class UpdateViewSet(UpdateAPIView):
    lookup_field='pk'
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class DeleteViewSet(DestroyAPIView):
    lookup_field='pk'
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class CreateViewSet(CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=CreateSerializer