from typing import Any

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView
from ..utils.permissions import is_own_user


class IsAuthor(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
        return is_own_user(request, obj)
