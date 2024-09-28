from django_filters import rest_framework as filters
from common.rest_framework.filters import FilterLookupExpr
from nation.models import (
    CountryModel, 
    CityModel, 
    AreaModel,
)


class CountryFilter(filters.FilterSet):
    class Meta:
        model = CountryModel
        fields = {
            'name': FilterLookupExpr.STRING,
            'short_code': FilterLookupExpr.STRING,
        }


class CityFilter(filters.FilterSet):
    class Meta:
        model = CityModel
        fields = {
            'name': FilterLookupExpr.STRING,
        }


class AreaFilter(filters.FilterSet):
    class Meta:
        model = AreaModel
        fields = {
            'name': FilterLookupExpr.STRING,
            'zip_code': FilterLookupExpr.NUMBER,
        }
