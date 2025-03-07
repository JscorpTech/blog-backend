from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import MediaModel


@admin.register(MediaModel)
class MediaAdmin(ModelAdmin):
    search_fields = ['file', "id"]
    list_display = (
        "id",
        "file",
        "__str__",
    )
