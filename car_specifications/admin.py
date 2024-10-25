from django.contrib import admin
from .models import Brand
from .models import Car
from .models import Model

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Model)


