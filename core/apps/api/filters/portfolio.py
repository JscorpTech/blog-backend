from django_filters import rest_framework as filters

from ..models import EducationModel, ExperienceModel, ProjectModel, StackCategoryModel, StackModel


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ProjectModel
        fields = ("name",)


class ExperienceFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ExperienceModel
        fields = ("name",)


class EducationFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = EducationModel
        fields = ("name",)


class StackFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = StackModel
        fields = ("name",)


class StackCategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = StackCategoryModel
        fields = ("name",)
