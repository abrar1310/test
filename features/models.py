from django.db import models
import uuid
from car_specifications.models import Car

class Feature(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )
    
    mileage= models.DecimalField(
        max_digits=8,
        decimal_places=3
        )

    fuel= models.DecimalField(
        max_digits=8,
        decimal_places=3,
        )
    
    type= models.CharField(
        max_length=40
        )
    
    class Meta:
        db_table = "feature"

class CarFeature(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )
    
    car= models.ForeignKey(
        Car,
        on_delete= models.DO_NOTHING,
        null=True,
        blank=True
        )

    feature= models.ForeignKey(
        Feature,
        on_delete= models.DO_NOTHING,
        null=True,
        blank=True
        )
    
    mileage= models.DecimalField(
        max_digits=8,
        decimal_places=3,
        null=True,
        blank=True
        )

    fuel= models.DecimalField(
        max_digits=8,
        decimal_places=3,
        null=True,
        blank=True
        )
    
    type= models.CharField(
        max_length=40,
        null=True,
        blank=True
        )
    
    class Meta:
        db_table = "car_feature"


