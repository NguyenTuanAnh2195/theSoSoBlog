from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import BlogpostSerializer


class CreateBlogPostView(CreateAPIView):
    serializer_class = BlogpostSerializer()
    permission_classes = [IsAuthenticated]


class RetrieveBlogPostView(RetrieveAPIView):
    serializer_class = BlogpostSerializer()
    permission_classes = [AllowAny]


class UpdateBlogPostView(UpdateAPIView):
    serializer_class = BlogpostSerializer()
    permission_classes = [IsAuthenticated]


class DeleteBlogPostView(DestroyAPIView):
    serializer_class = BlogpostSerializer()
    permission_classes = [IsAuthenticated]


class ListBlogPostView(ListAPIView):
    serializer_class = BlogpostSerializer()
    permission_classes = [IsAuthenticated]
