from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="get_token_view"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh_view"),
]
