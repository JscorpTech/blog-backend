from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from ..models import ContactModel
from ..serializers.contact import CreateContactSerializer, ListContactSerializer, RetrieveContactSerializer


@extend_schema(tags=["contact"])
class ContactView(BaseViewSetMixin, CreateModelMixin, GenericViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ListContactSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListContactSerializer,
        "retrieve": RetrieveContactSerializer,
        "create": CreateContactSerializer,
    }
