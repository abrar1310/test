from django.contrib import admin
from .models import Request
from .models import Admin

admin.site.register(Request)
admin.site.register(Admin)
