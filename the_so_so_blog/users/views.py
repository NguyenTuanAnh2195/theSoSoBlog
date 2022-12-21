from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..authentication.serializers import UserUpdatePasswordSerializer
from .permissions import IsSameUser
from .serializers import UserDetailSerializer

User = get_user_model()


class UserListView(ListAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()


class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()


class UserUpdateView(UpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsSameUser]
    queryset = User.objects.all()


class UserUpdatePasswordView(UpdateAPIView):
    serializer_class = UserUpdatePasswordSerializer
    permission_classes = [IsAuthenticated, IsSameUser]
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if self.request.user.id != user.id:
            raise PermissionDenied
        return super().update(request, args, kwargs)
