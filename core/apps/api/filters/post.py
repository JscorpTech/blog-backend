from django_filters import rest_framework as filters

from ..models import CategoryModel, PostModel, TagModel


class PostFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = PostModel
        fields = ("name",)


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = CategoryModel
        fields = ("name",)


class TagFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = TagModel
        fields = ("name",)
