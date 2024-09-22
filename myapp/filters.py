from django_filters import rest_framework as filters
from common.rest_framework .filters import FilterLookupExpr
from myapp.models import MyModel


class MyModelFilter(filters.FilterSet):
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