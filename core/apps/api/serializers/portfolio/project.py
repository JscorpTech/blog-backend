from rest_framework import serializers

from ...models import ProjectModel


class BaseProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = [
            "id",
            "name",
            "image",
            "desc",
            "source",
            "demo",
            "created_at",
            "updated_at"
        ]


class ListProjectSerializer(BaseProjectSerializer):
    class Meta(BaseProjectSerializer.Meta): ...


class RetrieveProjectSerializer(BaseProjectSerializer):
    class Meta(BaseProjectSerializer.Meta): ...


class CreateProjectSerializer(BaseProjectSerializer):
    class Meta(BaseProjectSerializer.Meta): ...
