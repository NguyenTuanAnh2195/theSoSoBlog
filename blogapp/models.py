from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogUser(User):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name='blog_posts', null=True, blank=True)

    def __str__(self):
        return f"<Post {self.title}>"
