from django.db import models
import uuid
from car_specifications.models import Car

class Image(models.Model):
    # id= models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    #     )
    
    img= models.ImageField(
        upload_to='images/'
    )

    car= models.ForeignKey(
        Car,
        on_delete= models.DO_NOTHING
    )

    class Meta:
        db_table = "images"
