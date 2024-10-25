from django.db import models
import uuid
from car_specifications.models import Car


class Purchase(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )
    
    date_of_sale= models.DateTimeField()

    date_of_rent= models.DateTimeField()

    date_of_return= models.DateTimeField()

    car= models.ForeignKey(
        Car,
        on_delete= models.DO_NOTHING,
        null= True,
        blank= True

    )

    class Meta:
        db_table = "purchase"

class Customer(models.Model):
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

    class Meta:
        db_table = "customer"


class CustomerPurchase(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )
    
    purchase= models.ForeignKey(
        Purchase,
        on_delete= models.DO_NOTHING
    )

    customer= models.ForeignKey(
        Customer,
        on_delete= models.DO_NOTHING

    )

    class Meta:
        db_table= "Customer_Purchase"


