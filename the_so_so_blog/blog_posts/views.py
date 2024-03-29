from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import BlogPost
from .serializers import BlogpostSerializer
from .permissions import IsAuthor


class CreateBlogPostView(CreateAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    throttle_classes = []

    def get_throttles(self):
        return super().get_throttles()


class RetrieveBlogPostView(RetrieveAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()


class UpdateBlogPostView(UpdateAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
    queryset = BlogPost.objects.all()


class DeleteBlogPostView(DestroyAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
    queryset = BlogPost.objects.all()


class ListBlogPostView(ListAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()
