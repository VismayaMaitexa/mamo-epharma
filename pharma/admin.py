from django.contrib import admin
from . models import Customer
from . models import Delivery_boy
from . models import Products
from . models import Address
from . models import Payment
from . models import Feedback

# Register your models here.
admin.site.register(Customer)
admin.site.register(Delivery_boy)
admin.site.register(Products)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Feedback)