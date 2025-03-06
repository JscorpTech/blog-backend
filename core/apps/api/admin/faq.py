from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from ..models import FaqCategoryModel, FaqModel


@admin.register(FaqModel)
class FaqAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "question",
        "__str__",
        "created_at",
        "updated_at"
    )


@admin.register(FaqCategoryModel)
class FaqcategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "__str__",
        "created_at",
        "updated_at"
    )
