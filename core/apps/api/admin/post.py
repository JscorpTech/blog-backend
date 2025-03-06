from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.decorators import display

from ..models import CategoryModel, PostModel, TagModel


@admin.register(PostModel)
class PostAdmin(ModelAdmin, TabbedTranslationAdmin):
    search_fields = ("title", "content",)
    autocomplete_fields = ("tags", "categories",)
    list_display = (
        "id",
        "title",
        "_views",
        "__str__",
        "created_at",
        "updated_at"
    )

    @display(label=True, ordering="views")
    def _views(self, obj):
        return obj.views


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    search_fields = ("name",)
    list_display = (
        "id",
        "__str__",
        "created_at",
        "updated_at"
    )


@admin.register(TagModel)
class TagAdmin(ModelAdmin, TabbedTranslationAdmin):
    search_fields = ("name",)
    list_display = (
        "id",
        "__str__",
        "created_at",
        "updated_at"
    )
