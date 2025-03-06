from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import display

from ..models import ContactModel


@admin.register(ContactModel)
class ContactAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
        "_phone",
        "title",
        "_content",
        "created_at",
        "updated_at",
    )

    @display()
    def _phone(self, obj) -> str:
        return obj.phone

    @display()
    def _content(self, obj) -> str:
        return obj.content[:50]
