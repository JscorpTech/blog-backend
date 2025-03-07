from django_core.serializers import AbstractTranslatedSerializer

from core.apps.shared.serializers import ListMediaSerializer
from ...models import ProjectModel


class BaseProjectSerializer(AbstractTranslatedSerializer):
    images = ListMediaSerializer(many=True)

    class Meta:
        model = ProjectModel
        fields = [
            "id",
            "name",
            "images",
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
