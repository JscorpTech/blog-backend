from rest_framework import serializers

from ...models import ContactModel


class BaseContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = [
            "id",
            "title",
            "content",
            "phone",
            "created_at",
            "updated_at"
        ]


class ListContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta): ...


class RetrieveContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta): ...


class CreateContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta): ...
