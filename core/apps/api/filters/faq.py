from django_filters import rest_framework as filters

from ..models import FaqCategoryModel, FaqModel


class FaqFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = FaqModel
        fields = ("name",)


class FaqcategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = FaqCategoryModel
        fields = ("name",)
