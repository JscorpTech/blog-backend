from rest_framework import serializers

from ...models import FaqModel


class BaseFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqModel
        fields = [
            "id",
            "question",
            "answer"
        ]


class ListFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...


class RetrieveFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...


class CreateFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...
