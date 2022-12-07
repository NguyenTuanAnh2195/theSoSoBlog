from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserDetailSerializer
from .permissions import IsSameUser
from ..authentication.serializers import UserUpdatePasswordSerializer

User = get_user_model()


class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]


class UserUpdateView(UpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsSameUser]


class UserUpdatePasswordView(UpdateAPIView):
    serializer_class = UserUpdatePasswordSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if self.request.user.id != user.id:
            raise PermissionDenied
        return super().update(request, args, kwargs)
