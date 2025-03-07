from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import CategoryModel, PostModel, TagModel
from ..serializers.post import (
    CreateCategorySerializer,
    CreatePostSerializer,
    CreateTagSerializer,
    ListCategorySerializer,
    ListPostSerializer,
    ListTagSerializer,
    RetrieveCategorySerializer,
    RetrievePostSerializer,
    RetrieveTagSerializer,
)


@extend_schema(tags=["post"])
class PostView(BaseViewSetMixin, ReadOnlyModelViewSet):
    serializer_class = ListPostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return PostModel.objects.prefetch_related("tags").prefetch_related("categories").order_by("-created_at").all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPostSerializer,
        "retrieve": RetrievePostSerializer,
        "create": CreatePostSerializer,
    }


@extend_schema(tags=["category"])
class CategoryView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = ListCategorySerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCategorySerializer,
        "retrieve": RetrieveCategorySerializer,
        "create": CreateCategorySerializer,
    }


@extend_schema(tags=["tag"])
class TagView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TagModel.objects.all()
    serializer_class = ListTagSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTagSerializer,
        "retrieve": RetrieveTagSerializer,
        "create": CreateTagSerializer,
    }
