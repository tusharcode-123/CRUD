from django.contrib import admin
from .models import customer,product,order
# Register your models here.

admin.site.register(customer)
admin.site.register(order)
admin.site.register(product)
