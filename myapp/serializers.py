from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from myapp.models import MyModel, User, ConfigurationModel


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
            'title',
            'char',
            'text',
            'integer',
            'start_date',
            'end_date',
            'price',
            'last_price',
            'address',
            'longitude',
            'latitude',
            'owner'
        )
        
    owner = CreateUserSerializer()
    last_price = serializers.FloatField()



class MyAppSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = (
            'id',
            'last_price',
            'owner',
        )
    
    last_price = serializers.FloatField()
    owner = CreateUserSerializer

 
class CreateMyAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = (
            'id',
            'title',
            'char',
            'text',
            'integer',
            'price',
            'start_date',
            'end_date',
            'address',
            'longitude',
            'latitude',
            'owner',
        )
        read_only_fields = ('owner', )

    def create(self, validated_data):
        if not self.context['request'].user.is_authenticated:
            raise ValueError('user is not authenticated')
        
        owner = self.context['request'].user
        validated_data['owner'] = owner
        return super().create(validated_data)
    
    def to_representation(self, instance):
        return MyAppSerializer(instance, context=self.context).data


class AdminMyAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = (
            'id',
            'title',
            'char',
            'text',
            'integer',
            'price',
            'last_price',
            'start_date',
            'end_date',
            'address',
            'longitude',
            'latitude',
            'owner'
        )


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigurationModel
        fields = (
            'id',
            'percentage_tax',
            'const_tax',
        )   
