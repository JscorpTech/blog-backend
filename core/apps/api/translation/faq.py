from modeltranslation.translator import TranslationOptions, register

from ..models import FaqCategoryModel, FaqModel


@register(FaqModel)
class FaqTranslation(TranslationOptions):
    fields = [
        "question",
        "answer",
    ]


@register(FaqCategoryModel)
class FaqCategoryTranslation(TranslationOptions):
    fields = [
        "name"
    ]
