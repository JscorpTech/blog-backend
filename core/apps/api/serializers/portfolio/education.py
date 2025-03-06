from rest_framework import serializers

from ...models import EducationModel


class BaseEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationModel
        fields = [
            "id",
            "name",
            "start_date",
            "end_date",
            "created_at",
            "updated_at"
        ]


class ListEducationSerializer(BaseEducationSerializer):
    class Meta(BaseEducationSerializer.Meta): ...


class RetrieveEducationSerializer(BaseEducationSerializer):
    class Meta(BaseEducationSerializer.Meta): ...


class CreateEducationSerializer(BaseEducationSerializer):
    class Meta(BaseEducationSerializer.Meta): ...
