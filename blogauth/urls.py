from django.urls import path
from .views import (
  BlogProfileDetailView,
  BlogProfileListView,
  ProfileRegisterView,
  ProfileLoginView,
  ProfileLogoutView,
  BlogProfileUpdateView,
)

app_name = 'accounts'
urlpatterns = [
    path('<int:pk>/', BlogProfileDetailView.as_view(), name='user-detail'),
    path('', BlogProfileListView.as_view(), name='user-list'),
    path('register/', ProfileRegisterView.as_view(), name='user-register'),
    path('<int:pk>/update', BlogProfileUpdateView.as_view(), name='user-update'),
    path('login/', ProfileLoginView.as_view(), name='login'),
    path('logout/', ProfileLogoutView.as_view(), name='logout'),
]
