from django.contrib.auth import password_validation
from django.core import exceptions
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import ModelSerializer

from the_so_so_blog.users.models import User


class BaseUserSerializer(ModelSerializer):
    password = CharField(allow_blank=False, allow_null=False, min_length=10, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")

        errors = {}
        try:
            password_validation.validate_password(password=password, user=user)
        except exceptions.ValidationError as exc:
            errors["password"] = list(exc.messages)

        if errors:
            raise ValidationError(errors)
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data["password"]
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserUpdatePasswordSerializer(BaseUserSerializer):
    class Meta:
        model = User
        fields = ["password"]

    def update(self, instance, validated_data):
        password = validated_data["password"]
        instance.set_password(password)
        instance.save()
        return instance
