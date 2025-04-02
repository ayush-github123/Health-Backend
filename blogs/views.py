from django.shortcuts import render
from rest_framework import generics
from blogs.models import Post
from blogs.serializers import BlogSerializer
from blogs.permissions import IsAuthorOrAdmin


class BlogListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

class BlogCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrAdmin]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrAdmin]



