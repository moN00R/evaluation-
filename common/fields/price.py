from typing import Any
from django.db import models
from django.core.exceptions import ValidationError


class Price(models.DecimalField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('max_digits', 12)
        kwargs.setdefault('decimal_places', 8)
        super().__init__(*args, **kwargs)
    
    def validate(self, value: Any, model_instance: models.Model) -> None:
        super().validate(value, model_instance)
        if value < 0:
            raise ValidationError('Price cannot be negative.')
        
