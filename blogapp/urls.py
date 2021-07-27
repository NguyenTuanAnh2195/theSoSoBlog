from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:post_id>like/', views.like, name='like-post'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete-post')
]
