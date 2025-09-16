from rest_framework import viewsets, permissions
from rest_framework.versioning import URLPathVersioning
from .models import Blog
from .serializers import BlogV1Serializer, BlogV2Serializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    versioning_class = URLPathVersioning   

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return BlogV2Serializer
        return BlogV1Serializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
