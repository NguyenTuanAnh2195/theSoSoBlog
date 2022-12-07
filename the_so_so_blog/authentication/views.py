from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView

from .serializers import BaseUserSerializer
from ..users.models import User


class RegisterView(CreateAPIView):
    serializer_class = BaseUserSerializer
    permission_classes = [AllowAny]



