from django.contrib import admin
from .models import CarFeature
from .models import Feature

admin.site.register(Feature)
admin.site.register(CarFeature)
