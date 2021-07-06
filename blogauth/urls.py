from django.urls import path

from .views import (
  BlogProfileDetailView,
  BlogProfileListView,
  ProfileRegisterView,
  ProfileLoginView,
)

app_name = 'accounts'
urlpatterns = [
    path('<int:pk>/', BlogProfileDetailView.as_view(), name='user-detail'),
    path('', BlogProfileListView.as_view(), name='user-list'),
    path('register/', ProfileRegisterView.as_view(), name='user-register'),
    path('login/', ProfileLoginView.as_view(), name='login'),
]
