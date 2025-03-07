from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class MediaModel(AbstractBaseModel):
    file = models.FileField(upload_to="media/", verbose_name=_("file"))

    def __str__(self):
        return self.file.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            file="Test.png",
        )

    class Meta:
        db_table = "media"
        verbose_name = _("MediaModel")
        verbose_name_plural = _("MediaModels")
