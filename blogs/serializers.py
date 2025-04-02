from rest_framework import serializers
from blogs.models import Post


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'created_at')
        read_only_fields = ('author', 'created_at')

