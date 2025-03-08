from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class PostModel(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    desc = models.CharField(max_length=1000, verbose_name=_("desc"))
    content = models.TextField(verbose_name=_("content"))
    image = models.ImageField(upload_to="post/", verbose_name=_("image"))
    views = models.IntegerField(default=0, verbose_name=_("views"))
    tags = models.ManyToManyField("TagModel", verbose_name=_("tags"), blank=True)
    categories = models.ManyToManyField("CategoryModel", verbose_name=_("categories"), blank=True)
    position = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            title="Test",
            content="Test",
            views=10,
            image="test.png",
        )

    class Meta:
        ordering = ["position"]
        db_table = "post"
        verbose_name = _("PostModel")
        verbose_name_plural = _("PostModels")


class CategoryModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "category"
        verbose_name = _("CategoryModel")
        verbose_name_plural = _("CategoryModels")


class TagModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "tag"
        verbose_name = _("TagModel")
        verbose_name_plural = _("TagModels")
