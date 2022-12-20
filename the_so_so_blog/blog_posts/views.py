from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import BlogpostSerializer
from .models import BlogPost

class CreateBlogPostView(CreateAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()


class RetrieveBlogPostView(RetrieveAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()


class UpdateBlogPostView(UpdateAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()


class DeleteBlogPostView(DestroyAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()


class ListBlogPostView(ListAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()
