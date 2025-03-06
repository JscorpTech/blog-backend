from rest_framework import serializers

from ...models import ExperienceModel


class BaseExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModel
        fields = [
            "id",
            "name",
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
