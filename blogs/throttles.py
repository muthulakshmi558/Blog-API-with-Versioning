from rest_framework.throttling import UserRateThrottle
from rest_framework.exceptions import Throttled
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Blog

class DailyPostThrottle(UserRateThrottle):
    scope = 'daily_post'

    def allow_request(self, request, view):
        if request.method == "POST" and request.user.is_authenticated:
            today = timezone.now().date()
            post_count = Blog.objects.filter(author=request.user, created_at__date=today).count()
            if post_count >= 5:
                raise Throttled(detail="Post limit (5/day) exceeded.")
        return True
