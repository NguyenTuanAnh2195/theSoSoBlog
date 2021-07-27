from django.db import models
from blogauth.models import BlogProfile
# Create your models here.


class Tag(models.Model):
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(BlogProfile, on_delete=models.CASCADE,
                               related_name='blog_posts', blank=False,
                               null=False)
    likers = models.ManyToManyField(BlogProfile, through='Like')
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def active_likes(self):
        return self.like_set.filter(active=True)


class Like(models.Model):
    liker = models.ForeignKey(BlogProfile,
                              on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
