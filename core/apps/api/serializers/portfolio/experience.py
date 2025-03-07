from rest_framework import serializers

from core.apps.shared.serializers import ListMediaSerializer
from ...models import ExperienceModel


class BaseExperienceSerializer(serializers.ModelSerializer):
    images = ListMediaSerializer(many=True, read_only=True)

    class Meta:
        model = ExperienceModel
        fields = [
            "id",
            "name",
            "role",
            "comments",
            "images",
            "start_date",
            "end_date",
            "created_at",
            "updated_at"
        ]


class ListExperienceSerializer(BaseExperienceSerializer):
    class Meta(BaseExperienceSerializer.Meta): ...


class RetrieveExperienceSerializer(BaseExperienceSerializer):
    class Meta(BaseExperienceSerializer.Meta): ...


class CreateExperienceSerializer(BaseExperienceSerializer):
    class Meta(BaseExperienceSerializer.Meta): ...
