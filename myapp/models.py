import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from common.audit.models import AuditModel
from common.fields.price import PriceField
from common.fields.location import LongitudeField, LatitudeField


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
    longitude = LongitudeField()
    latitude = LatitudeField() 

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
