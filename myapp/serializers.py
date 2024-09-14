from rest_framework import serializers
from myapp.models import MyModel, User
from django.contrib.auth.hashers import make_password


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'is_active',
        ) 
        read_only_fields = ('is_active',)

    def create(self, validated_data):
        password = validated_data.pop('password') 
        password = make_password(password)
        user = User.objects.create(
            password = password,
            **validated_data
        )
        return user


class MyAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = (
            'id',
            'char',
            'text',
            'integer',
            'time',
            'owner'
        )

    owner = CreateUserSerializer()


class MyAppSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = (
            'id',
            'owner'
        )
    
    owner = CreateUserSerializer

 
class CreateMyAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = (
            'id',
            'char',
            'text',
            'integer',
            'owner'
        )
        read_only_fields = ('owner', )

    def create(self, validated_data):
        owner = self.context['request'].user
        validated_data['owner'] = owner
        return super().create(validated_data)
    
    def to_representation(self, instance):
        return MyAppSerializers(instance, context=self.context).data


class AdminMyAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = (
            'id',
            'title',
            'char',
            'text',
            'integer',
            'is_active',
            'owner',
        )

