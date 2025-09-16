from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from .models import Blog

User = get_user_model()

class BlogAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="12345")
        self.client.login(username="admin", password="12345")

    def test_v1_create_blog(self):
        url = "/api/v1/blogs/"
        response = self.client.post(url, {"title": "V1 Blog", "content": "Basic content"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_v2_create_blog(self):
        url = "/api/v2/blogs/"
        response = self.client.post(url, {"title": "V2 Blog", "content": "Advanced", "category": "Tech", "tags": "django,api"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_v2_view_count_default(self):
        blog = Blog.objects.create(author=self.user, title="Check Views", content="test")
        url = f"/api/v2/blogs/{blog.id}/"
        response = self.client.get(url)
        self.assertEqual(response.data["view_count"], 0)

    def test_throttle_limit(self):
        url = "/api/v1/blogs/"
        for i in range(5):
            self.client.post(url, {"title": f"Post {i}", "content": "Spam"})
        response = self.client.post(url, {"title": "Limit", "content": "Exceeded"})
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
