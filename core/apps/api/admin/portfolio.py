from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import ArrayWidget
from adminsortable2.admin import SortableAdminMixin
from unfold.forms import ActionForm
from ..models import EducationModel, ExperienceModel, ProjectModel, StackCategoryModel, StackModel


@admin.register(ProjectModel)
class ProjectAdmin(SortableAdminMixin, ModelAdmin, TabbedTranslationAdmin):
    action_form = ActionForm
    search_fields = ["name", "id"]
    autocomplete_fields = ("images",)
    list_display = ("id", "source", "demo", "__str__", "created_at", "updated_at", "position")


@admin.register(ExperienceModel)
class ExperienceAdmin(SortableAdminMixin, ModelAdmin, TabbedTranslationAdmin):
    action_form = ActionForm
    list_display = ("id", "__str__", "created_at", "updated_at")
    search_fields = ["name"]
    autocomplete_fields = ("images",)
    formfield_overrides = {
        ArrayField: {"widget": ArrayWidget},
    }


@admin.register(EducationModel)
class EducationAdmin(SortableAdminMixin, ModelAdmin, TabbedTranslationAdmin):
    action_form = ActionForm
    list_display = ("id", "__str__", "created_at", "updated_at")


@admin.register(StackModel)
class StackAdmin(SortableAdminMixin, ModelAdmin, TabbedTranslationAdmin):
    action_form = ActionForm
    list_display = ("id", "__str__", "created_at", "updated_at")


@admin.register(StackCategoryModel)
class StackCategoryAdmin(SortableAdminMixin, ModelAdmin, TabbedTranslationAdmin):
    action_form = ActionForm
    list_display = (
        "id",
        "__str__",
    )
