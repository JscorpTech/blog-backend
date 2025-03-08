from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import EducationModel, ExperienceModel, ProjectModel, StackCategoryModel, StackModel
from ..serializers.portfolio import (
    CreateEducationSerializer,
    CreateExperienceSerializer,
    CreateProjectSerializer,
    CreateStackCategorySerializer,
    CreateStackSerializer,
    ListEducationSerializer,
    ListExperienceSerializer,
    ListProjectSerializer,
    ListStackCategorySerializer,
    ListStackSerializer,
    RetrieveEducationSerializer,
    RetrieveExperienceSerializer,
    RetrieveProjectSerializer,
    RetrieveStackCategorySerializer,
    RetrieveStackSerializer,
)


@extend_schema(tags=["project"])
class ProjectView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ProjectModel.objects.order_by("position")
    serializer_class = ListProjectSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListProjectSerializer,
        "retrieve": RetrieveProjectSerializer,
        "create": CreateProjectSerializer,
    }


@extend_schema(tags=["experience"])
class ExperienceView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ExperienceModel.objects.order_by("position")
    serializer_class = ListExperienceSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListExperienceSerializer,
        "retrieve": RetrieveExperienceSerializer,
        "create": CreateExperienceSerializer,
    }


@extend_schema(tags=["education"])
class EducationView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = EducationModel.objects.order_by("position")
    serializer_class = ListEducationSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListEducationSerializer,
        "retrieve": RetrieveEducationSerializer,
        "create": CreateEducationSerializer,
    }


@extend_schema(tags=["stack"])
class StackView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = StackModel.objects.order_by("position")
    serializer_class = ListStackSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListStackSerializer,
        "retrieve": RetrieveStackSerializer,
        "create": CreateStackSerializer,
    }


@extend_schema(tags=["stack category"])
class StackCategoryView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = StackCategoryModel.objects.order_by("position")
    serializer_class = ListStackCategorySerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListStackCategorySerializer,
        "retrieve": RetrieveStackCategorySerializer,
        "create": CreateStackCategorySerializer,
    }
