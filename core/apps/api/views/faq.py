from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import FaqCategoryModel
from ..serializers.faq import (
    CreateFaqCategorySerializer,
    ListFaqCategorySerializer,
    RetrieveFaqCategorySerializer,
)

@extend_schema(tags=["faq"])
class FaqView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = FaqCategoryModel.objects.all()
    serializer_class = ListFaqCategorySerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListFaqCategorySerializer,
        "retrieve": RetrieveFaqCategorySerializer,
        "create": CreateFaqCategorySerializer,
    }
