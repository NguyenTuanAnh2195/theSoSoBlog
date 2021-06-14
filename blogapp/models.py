from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<User {self.name}>"


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Post {self.title}>"
