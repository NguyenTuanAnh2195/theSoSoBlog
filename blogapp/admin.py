from django.contrib import admin

# Register your models here.
from .models import BlogUser, Post

admin.site.register(BlogUser)
admin.site.register(Post)
