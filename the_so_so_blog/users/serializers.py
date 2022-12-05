from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CharField, EmailField

from .models import User

class BaseUserSerializer(ModelSerializer):
    first_name = CharField(allow_null=True)
    last_name = CharField(allow_null=True)
    email = EmailField(allow_null=False, allow_blank=False)

