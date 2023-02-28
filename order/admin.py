from django.contrib import admin

# Register your models here.
from .models import Table, Order,MenuItem,OrderItem

admin.site.register(Table)
admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(OrderItem)