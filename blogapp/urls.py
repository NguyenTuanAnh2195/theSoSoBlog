from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(template_name='blogapp/index.html'), name='index'),
    path('users', views.BlogUserListView.as_view(), name='user_list'),
]

