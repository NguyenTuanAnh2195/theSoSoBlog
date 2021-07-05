from django.db import models
from django.contrib.auth.models import User
from blogauth.models import BlogProfile
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(BlogProfile, on_delete=models.CASCADE, related_name='blog_posts', blank=False, null=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
