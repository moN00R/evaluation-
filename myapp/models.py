from typing import Collection
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from common.audit.models import AuditModel
from common.singleton_model.models import SingletonModel 
from common.fields.price import PriceField
from common.fields.location import LongitudeField, LatitudeField


class ConfigurationModel(AuditModel):
    percentage_tax = models.FloatField()
    const_tax = models.FloatField()

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  

    
class MyModel(AuditModel):
    title = models.TextField()
    char = models.CharField(max_length=255)
    text = models.TextField()
    integer = models.IntegerField()
    is_active = models.BooleanField(default=True)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    price = PriceField()

    address = models.TextField(blank=True, null=True)
    longitude = LongitudeField(blank=True, null=True)
    latitude = LatitudeField(blank=True, null=True) 

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
