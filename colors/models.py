from django.db import models
import uuid
from car_specifications.models import Car

class Color(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )
    
    color_name= models.CharField(
        max_length=40
    )

    class Meta:
        db_table = "color"

    def __str__(self):
        return self.color_name


class CarColor(models.Model):
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

    color= models.ForeignKey(
        Color,
        on_delete= models.DO_NOTHING,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "car_color"

    def __str__(self):
        return f" {self.car} of color {self.color}"

