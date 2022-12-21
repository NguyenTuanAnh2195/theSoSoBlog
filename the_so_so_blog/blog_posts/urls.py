from django.urls import path

from the_so_so_blog.blog_posts.views import (
    CreateBlogPostView,
    DeleteBlogPostView,
    ListBlogPostView,
    RetrieveBlogPostView,
    UpdateBlogPostView,
)

urlpatterns = [
    path("create/", CreateBlogPostView.as_view(), name="create_post"),
    path("retrieve/<int:pk>", RetrieveBlogPostView.as_view(), name="retrieve_post"),
    path("update/<int:pk>", UpdateBlogPostView.as_view(), name="update_post"),
    path("delete/<int:pk>", DeleteBlogPostView.as_view(), name="delete_post"),
    path(
        "list/",
        ListBlogPostView.as_view(),
        name="list_post",
    ),
]
