from rest_framework import serializers

from ...models import StackCategoryModel
from .stack import ListStackSerializer


class BaseStackCategorySerializer(serializers.ModelSerializer):
    stacks = ListStackSerializer(many=True, read_only=True)

    class Meta:
        model = StackCategoryModel
        fields = [
            "id",
            "name",
            "stacks",
        ]


class ListStackCategorySerializer(BaseStackCategorySerializer):
    class Meta(BaseStackCategorySerializer.Meta): ...


class RetrieveStackCategorySerializer(BaseStackCategorySerializer):
    class Meta(BaseStackCategorySerializer.Meta): ...


class CreateStackCategorySerializer(BaseStackCategorySerializer):
    class Meta(BaseStackCategorySerializer.Meta): ...
