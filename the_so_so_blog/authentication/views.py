from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import BaseUserSerializer


class RegisterView(CreateAPIView):
    serializer_class = BaseUserSerializer
    permission_classes = [AllowAny]
