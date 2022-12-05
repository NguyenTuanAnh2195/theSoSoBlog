from django.db import models
from the_so_so_blog.users.models import User
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(blank=False, null=False, max_length=120)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    posts = models.ManyToManyField(BlogPost)
