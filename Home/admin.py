from itertools import product
from django.contrib import admin
from .models import Product, contactform

# Register your models here.
admin.site.register(Product)
admin.site.register(contactform)


