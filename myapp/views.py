# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from myapp.filters import MyModelFilter
from myapp.models import (
    MyModel, 
    User,
    )
from myapp.serializers import (
    MyAppSerializer, 
    MyAppSmallSerializer,
    CreateMyAppSerializer,
    AdminMyAppSerializer,
    CreateUserSerializer,
    )


class UserViewSet(ModelViewSet):
    http_method_names = ('get', 'post')
    queryset = User.objects.filter(is_active=True)
    serializer_class = CreateUserSerializer
    permission_classes = ()


class MyAppObjectsViewSet(ModelViewSet):
    http_method_names = ('get', 'post')
    permission_classes = ()

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            return MyAppSerializer
        return CreateMyAppSerializer
    
    def get_queryset(self):
        my_objects = self.request.user
        return MyModel.objects.filter(owner=my_objects)


class MyAppViewSet(ModelViewSet):
    http_method_names = ('get')
    queryset = MyModel.objects.all()
    permission_classes = ()
    serializer_class = MyAppSmallSerializer
    filterset_class = MyModelFilter


class AdminMyAppViewSet(ModelViewSet):
    queryset = MyModel.objects.all()
    permission_classes = (IsAdminUser, )
    serializer_class = AdminMyAppSerializer
    filterset_class = MyModelFilter

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)