from django.db import models
import uuid
from car_specifications.models import Car

class Shape(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )
    
    shape_name= models.CharField(
        max_length= 60
    )

    class Meta:
        db_table = "shape"

class CarShape(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )
    
    car= models.ForeignKey(
        Car,
        on_delete= models.DO_NOTHING
    )

    shape= models.ForeignKey(
        Shape,
        on_delete= models.DO_NOTHING,
        null= True,
        blank= True
    )

    shape_name= models.CharField(
        max_length= 60,
        null= True,
        blank= True
    )

    class Meta:
        db_table = "car_shape"
