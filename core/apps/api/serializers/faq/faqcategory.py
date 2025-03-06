from rest_framework import serializers

from .faq import ListFaqSerializer
from ...models import FaqCategoryModel


class BaseFaqCategorySerializer(serializers.ModelSerializer):
    faqs = ListFaqSerializer(many=True, read_only=True)

    class Meta:
        model = FaqCategoryModel
        fields = [
            "id",
            "name",
            "faqs",
        ]


class ListFaqCategorySerializer(BaseFaqCategorySerializer):
    class Meta(BaseFaqCategorySerializer.Meta): ...


class RetrieveFaqCategorySerializer(BaseFaqCategorySerializer):
    class Meta(BaseFaqCategorySerializer.Meta): ...


class CreateFaqCategorySerializer(BaseFaqCategorySerializer):
    class Meta(BaseFaqCategorySerializer.Meta): ...
