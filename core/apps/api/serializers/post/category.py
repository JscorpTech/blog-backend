from rest_framework import serializers

from ...models import CategoryModel


class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            "id",
            "name",
        ]


class ListCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...


class RetrieveCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...


class CreateCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...
