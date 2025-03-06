from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class FaqModel(AbstractBaseModel):
    category = models.ForeignKey("FaqCategoryModel", on_delete=models.CASCADE, related_name="faqs")
    question = models.CharField(_("question"), max_length=255)
    answer = models.CharField(_("answer"), max_length=255)

    def __str__(self):
        return self.question

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            category=FaqCategoryModel._create_fake(),
            question="Test",
            answer="Test",
        )

    class Meta:
        db_table = "faq"
        verbose_name = _("FaqModel")
        verbose_name_plural = _("FaqModels")


class FaqCategoryModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "faqcategory"
        verbose_name = _("Faq Category Model")
        verbose_name_plural = _("Faq Category Models")
