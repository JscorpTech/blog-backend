from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from ..models import EducationModel, ExperienceModel, ProjectModel, StackCategoryModel, StackModel


@admin.register(ProjectModel)
class ProjectAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "source", "demo", "__str__", "created_at", "updated_at")


@admin.register(ExperienceModel)
class ExperienceAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "__str__", "created_at", "updated_at")


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
