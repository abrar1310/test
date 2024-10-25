from django.db import models
import uuid
from django.core.validators import MinValueValidator


class Brand(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )

    brand= models.CharField(
        max_length=50,
    )
    
    class Meta:
        db_table = "brand"


    def __str__ (self):
        return self.brand

class Car(models.Model):
    AVAILABLE = 'available'
    SOLD = 'sold'
    RESERVED = 'reserved'
    FOR_RENT = 'for_rent'
    RENTED = 'rented'
    NOT_FOR_SALE = 'not_for_sale'

    STATUS_CHOICES = [
        (AVAILABLE,'For Sale'),
        (SOLD, 'SOLD'),
        (RESERVED,'Reserved'),
        (FOR_RENT,'For Rent'),
        (RENTED,'Rented'),
        (NOT_FOR_SALE,'Not For Sale')
        ]
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )
    
    status= models.CharField(
        max_length= 50,
        choices= STATUS_CHOICES,
        default= AVAILABLE,
        )


    price= models.DecimalField(
        max_digits=20,
        decimal_places=4,
        null=True,
        blank=True
        )
    
    quantity= models.IntegerField(
        #default = 0, بالامكان كذلك تحديد القيمة هكذا .. 
        validators=[MinValueValidator(0)],
        null=True,
        blank=True
        )

    brand= models.ForeignKey(
        Brand,
        on_delete= models.DO_NOTHING,
        null=True,
        blank=True
        )

    class Meta:
        db_table = "car"
    
    def __str__(self):
        return f"the car Brand is: {self.brand} ,its status is: {self.status}"

class Model(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )

    model= models.CharField(
        max_length=50
        )

    brand= models.ForeignKey(
        Brand,
        on_delete= models.DO_NOTHING,
        null=True,   # كتير مهمين عفكرة بيضرب الشغل اذا ما كنا حاطين للحقول امكانية تكون فارغة 
        blank=True
            )
    
    class Meta:
        db_table = "model"

    def __str__(self):
        return f"Model {self.model} of brand {self.brand}"


