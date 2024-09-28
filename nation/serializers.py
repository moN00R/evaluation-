from rest_framework import serializers
from nation.models import CountryModel, CityModel, AreaModel


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = (
            'id',
            'name',
            'short_code'
        )
    

class GetCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = (
            'id',
            'name',
            'country',
        )

    country = CountrySerializer()


class GetAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaModel
        fields = (
            'id',
            'name',
            'zip_code',
            'city',
        ) 

    city = GetCitySerializer()


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = (
            'id',
            'name',
            'country',
        )

    def to_representation(self, instance):
        return GetCitySerializer(instance, context=self.context).data
    

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaModel
        fields = (
            'id',
            'name',
            'zip_code',
            'city',
        ) 

    def to_representation(self, instance):
        return GetAreaSerializer(instance, context=self.context).data
