from django.contrib import admin

# Register your models here.
from .models import Table, Order,MenuItem

admin.site.register(Table)
admin.site.register(Order)
admin.site.register(MenuItem)