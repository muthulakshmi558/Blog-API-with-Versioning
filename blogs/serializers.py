from rest_framework import serializers
from .models import Blog

class BlogV1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author']
        read_only_fields = ['author']

class BlogV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'category', 'tags', 'view_count', 'author']
        read_only_fields = ['author', 'view_count']
