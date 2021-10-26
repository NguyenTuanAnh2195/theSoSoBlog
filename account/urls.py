from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.UserListView.as_view(), name='index'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
