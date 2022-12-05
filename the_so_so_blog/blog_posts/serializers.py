from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CharField
from django.conf import settings
from the_so_so_blog.users.serializers import BaseUserSerializer


class BlogpostSerializer(ModelSerializer):
    title = CharField(allow_blank=False, allow_null=False, max_length=settings.BLOG_TITLE_MAX_LENGTH)
    content = CharField()
    author = BaseUserSerializer()

    def create(self, validated_data):
        validated_data["author"] = self.context["requests"].user
        return super().create(validated_data)


