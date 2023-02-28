from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order,OrderItem

# @receiver(pre_save,sender=Order)

# def IncludeOrderItem(sender,instance,created,**kwargs):
#     pass
 