from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.renderers import BaseRenderer


class PlainTextRenderer(BaseRenderer):
    media_type = 'text/plain'
    format = 'txt'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return str(data)


@extend_schema(tags=["health"])
class HealthView(APIView):
    renderer_classes = (PlainTextRenderer,)
    permission_classes = [AllowAny]

    def get(self, request):
        return Response("OK", status=status.HTTP_200_OK)
