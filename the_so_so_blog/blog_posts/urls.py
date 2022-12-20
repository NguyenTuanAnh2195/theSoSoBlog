from django.urls import re_path

from the_so_so_blog.blog_posts.views import (
    CreateBlogPostView,
    RetrieveAPIView,
    UpdateBlogPostView,
    DeleteBlogPostView,
    ListBlogPostView,
)

urlpatterns = [
    re_path("create/", CreateBlogPostView.as_view(), name="create_post"),
    re_path("retrieve/<int:pk>", RetrieveAPIView.as_view(), name="retrieve_post"),
    re_path("update/<int:pk>", UpdateBlogPostView.as_view(), name="update_post"),
    re_path("delete/<int:pk>", DeleteBlogPostView.as_view(), name="delete_post"),
    re_path("list/", ListBlogPostView.as_view(), name="list_post",)
]
