import django_filters
from django.db.models import F, ExpressionWrapper, DecimalField
from django_filters import rest_framework as filters
from common.rest_framework.filters import FilterLookupExpr
from myapp.models import MyModel, ConfigurationModel


class MyModelFilter(filters.FilterSet):
    last_price_lte = django_filters.NumberFilter(method='filter_by_last_price_lte')
    last_price_lt = django_filters.NumberFilter(method='filter_by_last_price_lt')
    last_price_gte = django_filters.NumberFilter(method='filter_by_last_price_gte')
    last_price_gt = django_filters.NumberFilter(method='filter_by_last_price_gt')
    class Meta:
        model = MyModel
        fields = {
            'title' : FilterLookupExpr.STRING,
            'char': FilterLookupExpr.STRING,
            'text': FilterLookupExpr.STRING,
            'integer': FilterLookupExpr.NUMBER,
            'start_date': FilterLookupExpr.DATETIME,
            'end_date': FilterLookupExpr.DATETIME,
            'price': FilterLookupExpr.NUMBER,
            'address': FilterLookupExpr.STRING,
            'owner': FilterLookupExpr.OTHER
        }
    
    def filter_by_last_price_lt(self, queryset, name, value):
        tax = ConfigurationModel.objects.first()
        const_tax = tax.const_tax
        percentage_tax = tax.percentage_tax
        last_price = (float(value) - const_tax) / (1 + percentage_tax / 100)
        return queryset.filter(price__lt=last_price)

    def filter_by_last_price_lte(self, queryset, name, value):
        tax = ConfigurationModel.objects.first()
        const_tax = tax.const_tax
        percentage_tax = tax.percentage_tax
        last_price = (float(value) - const_tax) / (1 + percentage_tax / 100)
        return queryset.filter(price__lte=last_price)

    def filter_by_last_price_gt(self, queryset, name, value):
        tax = ConfigurationModel.objects.first()
        const_tax = tax.const_tax
        percentage_tax = tax.percentage_tax
        last_price = (float(value) - const_tax) / (1 + percentage_tax / 100)
        return queryset.filter(price__gt=last_price)

    def filter_by_last_price_gte(self, queryset, name, value):
        tax = ConfigurationModel.objects.first()
        const_tax = tax.const_tax
        percentage_tax = tax.percentage_tax
        last_price = (float(value) - const_tax) / (1 + percentage_tax / 100)
        return queryset.filter(price__gte=last_price)


class MyModelFilterSecond(filters.FilterSet):
    last_price_lte = django_filters.NumberFilter(field_name='last_price', lookup_expr='lte')
    last_price_lt = django_filters.NumberFilter(field_name='last_price', lookup_expr='lt')
    last_price_gte = django_filters.NumberFilter(field_name='last_price', lookup_expr='gte')
    last_price_gt = django_filters.NumberFilter(field_name='last_price', lookup_expr='gt')

    class Meta:
        model = MyModel
        fields = {
            'title' : FilterLookupExpr.STRING,
            'char': FilterLookupExpr.STRING,
            'text': FilterLookupExpr.STRING,
            'integer': FilterLookupExpr.NUMBER,
            'start_date': FilterLookupExpr.DATETIME,
            'end_date': FilterLookupExpr.DATETIME,
            'price': FilterLookupExpr.NUMBER,
            'address': FilterLookupExpr.STRING,
            'owner': FilterLookupExpr.OTHER
        }
    