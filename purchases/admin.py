from django.contrib import admin
from .models import Purchase
from .models import Customer
from .models import CustomerPurchase

admin.site.register(Purchase)
admin.site.register(Customer)
admin.site.register(CustomerPurchase)
