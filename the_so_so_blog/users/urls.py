from django.urls import path

from the_so_so_blog.users.views import (
    UserDetailView,
    UserUpdateView,
    UserUpdatePasswordView,
    UserListView,
)

app_name = "users"
urlpatterns = [
    path("", view=UserListView.as_view(), name="user_list"),
    path("<int:pk>/update", view=UserUpdateView.as_view(), name="user_update"),
    path("<int:pk>/", view=UserDetailView.as_view(), name="user_detail"),
    path("<int:pk>/update-password/", view=UserUpdatePasswordView.as_view(), name="update_password"),
]
