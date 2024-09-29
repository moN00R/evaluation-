from django.db import models
from common.audit.models import AuditModel


class CountryModel(AuditModel):
    name = models.CharField(max_length=20)
    short_code = models.CharField(max_length=3)


class CityModel(AuditModel):
    name = models.CharField(max_length=20)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, related_name='cities')


class AreaModel(AuditModel):
    name = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name='areas') 
