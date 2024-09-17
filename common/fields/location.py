from typing import Any
from django.db import models
from django.core.exceptions import ValidationError


class LatitudeField(models.FloatField):
    def validate(self, value: Any, model_instance: models.Model) -> None:
        super().validate(value, model_instance)
        if value < -90 or value < 90:
            raise ValidationError('Latitude must be between -90 and 90.')

class LongitudeField(models.FloatField):
    def validate(self, value: Any, model_instance: models.Model) -> None:
        super().validate(value, model_instance)
        if value < -180 or value > 180:
            raise ValidationError('Longitude must be between 180 and -180.')
        
