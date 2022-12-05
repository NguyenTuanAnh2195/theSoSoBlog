from django.urls import re_path

from the_so_so_blog.blog_posts.views import (
    CreateBlogPostView,
)

urlpatterns = [
    re_path("create/", CreateBlogPostView.as_view(), name="")
]
