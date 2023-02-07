from django.conf import settings
from rest_framework.fields import CharField, ChoiceField
from rest_framework.serializers import ModelSerializer

from the_so_so_blog.users.serializers import UserDetailSerializer

from .models import BlogPost


class BlogpostSerializer(ModelSerializer):
    title = CharField(allow_blank=False, allow_null=False, max_length=settings.BLOG_TITLE_MAX_LENGTH)
    content = CharField()
    author = UserDetailSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = ["title", "content", "author", "created_at", "updated_at", "id", "category"]

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
