import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

from core.apps.shared.models import MediaModel


class ProjectModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    desc = models.CharField(_("description"), max_length=255)
    images = models.ManyToManyField(MediaModel, verbose_name=_("images"))
    source = models.URLField(verbose_name=_("source"), null=True, blank=True)
    demo = models.URLField(verbose_name=_("demo"), null=True, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
            desc="Test",
            image="Test.png",
        )

    class Meta:
        db_table = "project"
        verbose_name = _("ProjectModel")
        verbose_name_plural = _("ProjectModels")


class ExperienceModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    comments = ArrayField(base_field=models.CharField(verbose_name=_("comments"), max_length=255),
                          verbose_name=_("comments"), null=True, blank=True)
    images = models.ManyToManyField(MediaModel, verbose_name=_("images"))
    role = models.CharField(verbose_name=_("role"), max_length=255)
    start_date = models.DateField(verbose_name=_("start date"))
    end_date = models.DateField(verbose_name=_("end date"), null=True, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
        )

    class Meta:
        db_table = "experience"
        verbose_name = _("ExperienceModel")
        verbose_name_plural = _("ExperienceModels")


class EducationModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    start_date = models.DateField(verbose_name=_("start date"))
    end_date = models.DateField(verbose_name=_("end date"), null=True, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
        )

    class Meta:
        db_table = "education"
        verbose_name = _("EducationModel")
        verbose_name_plural = _("EducationModels")


class StackModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    category = models.ForeignKey("StackCategoryModel", verbose_name=_("category"), related_name="stacks",
                                 on_delete=models.CASCADE)
    image = models.ImageField(upload_to="stack/", verbose_name=_("image"))

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
            category=StackCategoryModel._create_fake(),
            image="Test.png",
        )

    class Meta:
        db_table = "stack"
        verbose_name = _("StackModel")
        verbose_name_plural = _("StackModels")


class StackCategoryModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "stackcategory"
        verbose_name = _("Stack CategoryModel")
        verbose_name_plural = _("Stack CategoryModels")
