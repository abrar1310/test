from django.db import models
import uuid
from car_specifications.models import Car

class Request(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )
    
    name= models.CharField(
        max_length= 50
    )

    email= models.EmailField(
        max_length= 50,
        unique=True
    )

    password= models.CharField(
        max_length=128
    )

    phone= models.CharField(
        max_length=30,
        unique= True
    )

    date= models.DateTimeField()

    area= models.CharField(
        max_length= 50,
    )

    is_done= models.BooleanField()

    car= models.ForeignKey(
        Car,
        on_delete= models.DO_NOTHING,
        null= True,
        blank= True
    )

    class Meta:
        db_table = "request"


class Admin(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )
    name= models.CharField(
        max_length= 50
    )

    email= models.EmailField(
        max_length= 50,
        unique=True
    )

    password= models.CharField(
        max_length=128
    )

    phone= models.CharField(
        max_length=30,
        unique= True
    )

    request= models.ForeignKey(
        Request,
        on_delete= models.DO_NOTHING,
        null= True,
        blank= True
    )

    class Meta:
        db_table = "admin"

