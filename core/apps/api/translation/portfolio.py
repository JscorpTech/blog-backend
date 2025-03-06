from modeltranslation.translator import TranslationOptions, register

from ..models import EducationModel, ExperienceModel, ProjectModel, StackModel, StackCategoryModel


@register(ProjectModel)
class ProjectTranslation(TranslationOptions):
    fields = [
        "name",
        "desc",
    ]


@register(ExperienceModel)
class ExperienceTranslation(TranslationOptions):
    fields = [
        "name",
    ]


@register(EducationModel)
class EducationTranslation(TranslationOptions):
    fields = [
        "name",
    ]


@register(StackModel)
class StackTranslation(TranslationOptions):
    fields = [
        "name",
    ]


@register(StackCategoryModel)
class StackCategoryTranslation(TranslationOptions):
    fields = [
        "name",
    ]
