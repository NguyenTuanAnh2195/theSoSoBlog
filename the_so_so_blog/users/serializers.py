from rest_framework.serializers import ModelSerializer

from .models import User


class UserDetailAdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "avatar",
            "is_active",
            "is_admin",
            "country",
            "city",
            "address",
            "email",
            "id",
        ]


class UserDetailSerializer(UserDetailAdminSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "avatar", "country", "city", "address", "email", "id"]
