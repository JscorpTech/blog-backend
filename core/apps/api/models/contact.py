from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ContactModel(AbstractBaseModel):
    title = models.CharField(_("title"), max_length=255)
    content = models.TextField(_("content"))
    phone = models.CharField(_("phone"), max_length=255)

    def __str__(self):
        return self.title

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
            content="salom",
            phone="+998888112309",
        )

    class Meta:
        db_table = "contact"
        verbose_name = _("ContactModel")
        verbose_name_plural = _("ContactModels")
