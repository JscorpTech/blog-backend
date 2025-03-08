from rest_framework import serializers

from .tag import ListTagSerializer
from .category import ListCategorySerializer
from ...models import PostModel


class BasePostSerializer(serializers.ModelSerializer):
    tags = ListTagSerializer(many=True, read_only=True)
    categories = ListCategorySerializer(many=True, read_only=True)

    class Meta:
        model = PostModel
        fields = [
            "id",
            "title",
            "views",
            "image",
            "desc",
            "tags",
            "categories",
            "created_at",
            "updated_at",
        ]


class ListPostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta): ...


class RetrievePostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta):
        fields = BasePostSerializer.Meta.fields + [
            "content",
        ]


class CreatePostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta): ...
