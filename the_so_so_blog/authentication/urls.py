from django.urls import re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView

urlpatterns = [
    re_path("token/", TokenObtainPairView.as_view(), name="get_token_view"),
    re_path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh_view"),
    re_path("register/", RegisterView.as_view(), name="user_register_view"),
]
