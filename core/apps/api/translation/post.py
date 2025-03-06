from modeltranslation.translator import TranslationOptions, register

from ..models import CategoryModel, PostModel, TagModel


@register(PostModel)
class PostTranslation(TranslationOptions):
    fields = [
        "title",
        "content"
    ]


@register(CategoryModel)
class CategoryTranslation(TranslationOptions):
    fields = [
        "name",
    ]


@register(TagModel)
class TagTranslation(TranslationOptions):
    fields = [
        "name",
    ]
