# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
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


class MyAppViewSet(ModelViewSet):
    http_method_names = ('get', 'post')
    permission_classes = ()
    queryset = MyModel.objects.all()
    
    def list(self, request, *args, **kwargs):
        response_data = []
        objects = self.queryset
        for object in objects:
            if object.owner == self.request.user:
                serializer = MyAppSerializer(object)
            else:
                serializer = MyAppSmallSerializer(object)
            
            response_data.append(serializer.data)

        return Response(response_data)

    def retrieve(self, request, *args, **kwargs):
        object = self.get_object()
        if object.owner == self.request.user:
            serializer = MyAppSerializer(object)
        else:
            serializer = MyAppSmallSerializer(object)

        return Response(serializer.data)
        
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateMyAppSerializer
        return MyAppSerializer    


class UserViewSet(ModelViewSet):
    http_method_names = ('get', 'post')
    queryset = User.objects.filter(is_active=True)
    serializer_class = CreateUserSerializer
    permission_classes = ()


class AdminMyAppViewSet(ModelViewSet):
    queryset = MyModel.objects.all()
    permission_classes = (IsAdminUser, )
    serializer_class = AdminMyAppSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)