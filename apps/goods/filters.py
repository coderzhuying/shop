import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(field_name="shop_price", help_text="本店价格小于或等于", lookup_expr="gte")
    # 参数大于本店价格

    pricemax = django_filters.NumberFilter(field_name="shop_price", help_text="本店价格大于或等于", lookup_expr="lte")
    # 参数小于本店价格

    top_category = django_filters.NumberFilter(method="top_category_filter")
    # 某个类目下所有商品的数量

    # name = django_filters.CharFilter(field_name="name", help_text="商品名", lookup_expr="icontains")
    # 模糊查询

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) |
                               Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['name', 'pricemax', 'pricemax', 'top_category', 'is_hot', 'is_new']
