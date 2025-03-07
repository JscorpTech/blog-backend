from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import  ArrayWidget

from ..models import EducationModel, ExperienceModel, ProjectModel, StackCategoryModel, StackModel


@admin.register(ProjectModel)
class ProjectAdmin(ModelAdmin, TabbedTranslationAdmin):
    search_fields = ['name', "id"]
    autocomplete_fields = ("images",)
    list_display = ("id", "source", "demo", "__str__", "created_at", "updated_at")


@admin.register(ExperienceModel)
class ExperienceAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "__str__", "created_at", "updated_at")
    search_fields = ["name"]
    autocomplete_fields = ("images",)
    formfield_overrides = {
        ArrayField: {"widget": ArrayWidget},
    }


@admin.register(EducationModel)
class EducationAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "__str__", "created_at", "updated_at")


@admin.register(StackModel)
class StackAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "__str__", "created_at", "updated_at")


@admin.register(StackCategoryModel)
class StackCategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "__str__",
    )
