from rest_framework import serializers

from ...models import StackModel


class BaseStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StackModel
        fields = [
            "id",
            "name"
        ]


class ListStackSerializer(BaseStackSerializer):
    class Meta(BaseStackSerializer.Meta): ...


class RetrieveStackSerializer(BaseStackSerializer):
    class Meta(BaseStackSerializer.Meta): ...


class CreateStackSerializer(BaseStackSerializer):
    class Meta(BaseStackSerializer.Meta): ...
