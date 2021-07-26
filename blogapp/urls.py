from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('like/<int:post_id>', views.like, name='like-post'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete-post')
]
