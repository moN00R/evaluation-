# from rest_framework.permissions import IsAuthenticated
from django.db.models import F, ExpressionWrapper, DecimalField
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from myapp.filters import MyModelFilter, MyModelFilterSecond
from myapp.models import (
    MyModel, 
    User,
    ConfigurationModel,
    )
from myapp.serializers import (
    MyAppSerializer, 
    MyAppSmallSerializer,
    CreateMyAppSerializer,
    # AdminMyAppSerializer,
    CreateUserSerializer,
    TaxSerializer,
    )


class UserViewSet(ModelViewSet):
    http_method_names = ('get', 'post')
    queryset = User.objects.filter(is_active=True)
    serializer_class = CreateUserSerializer
    permission_classes = ()


class MyAppObjectsViewSet(ModelViewSet):
    http_method_names = ('get', 'post')
    permission_classes = ()
    filterset_class = MyModelFilterSecond
    serializer_class_method_app = {
        'GET':MyAppSerializer,
        'POST':CreateMyAppSerializer
        }
    
    def get_serializer_class(self):
        return self.serializer_class_method_app[self.request.method]
    
    def get_queryset(self):
        user = self.request.user
        queryset = MyModel.objects.filter(owner=user)
        
        tax = ConfigurationModel.objects.first()
        if not tax:
            return queryset  

        const_tax = tax.const_tax
        percentage_tax = tax.percentage_tax

        queryset = queryset.annotate(
            last_price=ExpressionWrapper(
                F('price') + (F('price') * percentage_tax / 100) + const_tax,
                output_field=DecimalField()
            )
        )
        return queryset


class MyAppViewSet(ModelViewSet):
    http_method_names = ('get')
    permission_classes = ()
    queryset = MyModel.objects.all()
    serializer_class = MyAppSmallSerializer
    filterset_class = MyModelFilterSecond

    def get_queryset(self):
        queryset = super().get_queryset()

        tax = ConfigurationModel.objects.first()
        if not tax:
            return queryset  

        const_tax = tax.const_tax
        percentage_tax = tax.percentage_tax

        queryset = queryset.annotate(
            last_price=ExpressionWrapper(
                F('price') + (F('price') * percentage_tax / 100) + const_tax,
                output_field=DecimalField()
            )
        )
        return queryset


class AdminMyAppViewSet(ModelViewSet):
    queryset = MyModel.objects.all()
    permission_classes = (IsAdminUser, )
    filterset_class = MyModelFilterSecond
    serializer_class_method_map = {
        'GET':MyAppSerializer,
        'POST':CreateUserSerializer
        }

    def get_serializer_class(self):
        return self.serializer_class_method_map[self.request.method]
    
    def get_queryset(self):
        queryset = super().get_queryset()

        tax = ConfigurationModel.objects.first()
        if not tax:
            return queryset  

        const_tax = tax.const_tax
        percentage_tax = tax.percentage_tax

        queryset = queryset.annotate(
            last_price=ExpressionWrapper(
                F('price') + (F('price') * percentage_tax / 100) + const_tax,
                output_field=DecimalField()
            )
        )
        return queryset


class ConfigurationViewSet(ModelViewSet):
    queryset = ConfigurationModel.objects.all()
    http_method_names = ('get', 'post')
    serializer_class = TaxSerializer
    permission_classes = (IsAdminUser, )
