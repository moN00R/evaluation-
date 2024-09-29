from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from nation.models import (
    CountryModel, 
    CityModel, 
    AreaModel,
)
from nation.serializers import (
    CountrySerializer,
    CitySerializer, 
    AreaSerializer,
    GetCitySerializer,
    GetAreaSerializer,
)

from nation.filters import (
    CountryFilter,
    CityFilter,
    AreaFilter
)


class AdminCountryViewSet(ModelViewSet):
    queryset = CountryModel.objects.all().prefetch_related('cities')
    permission_classes = (IsAdminUser, )
    serializer_class = CountrySerializer
    filterset_class = CountryFilter


class AdminCityViewSet(ModelViewSet):
    queryset = CityModel.objects.all().prefetch_related('areas')
    permission_classes = (IsAdminUser, )
    filterset_class = CityFilter
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetCitySerializer
        return CitySerializer


class AdminAreaViewSet(ModelViewSet):
    queryset = AreaModel.objects.all()
    permission_classes = (IsAdminUser, )
    filterset_class = AreaFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetAreaSerializer
        return AreaSerializer


# ------------------------------------------------------------------------------#
    
class CountryViewSet(ModelViewSet):
    http_method_names = ('get', )
    queryset = CountryModel.objects.all().prefetch_related('cities')
    permission_classes = (IsAuthenticated, )
    serializer_class = CountrySerializer
    filterset_class = CountryFilter
 

class CityViewSet(ModelViewSet):
    http_method_names = ('get', )
    queryset = CityModel.objects.all().prefetch_related('areas')
    permission_classes = (IsAuthenticated, )
    serializer_class = GetCitySerializer
    filterset_class = CityFilter


class AreaViewSet(ModelViewSet):
    http_method_names = ('get', )
    queryset = AreaModel.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = GetAreaSerializer
    filterset_class = AreaFilter
