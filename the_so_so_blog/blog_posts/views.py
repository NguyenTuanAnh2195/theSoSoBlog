from typing import List

from rest_framework.generics import CreateAPIView, UsesQuerySet, UpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import BlogpostSerializer


class CreateBlogPostView(CreateAPIView):
    serializer_class = BlogpostSerializer()
    permission_classes = [IsAuthenticated]


class UpdateBlogPostView(UpdateAPIView):
    serializer_class = BlogpostSerializer()
    permission_classes = [IsAuthenticated]


class ListBlogPostView(ListAPIView):
    serializer_class = BlogpostSerializer()
    permission_classes = [IsAuthenticated]
