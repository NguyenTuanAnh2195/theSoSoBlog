from django.urls import path

from the_so_so_blog.users.views import (
    UserDetailView,
    UserUpdateView,
    UserUpdatePasswordView,
)

app_name = "users"
urlpatterns = [
    path("<int:pk>/update", view=UserUpdateView.as_view(), name="user_update"),
    path("<int:pk>/", view=UserDetailView.as_view(), name="user_detail"),
    path("<int:pk>/update-password/", view=UserUpdatePasswordView.as_view(), name="update_password"),
]
