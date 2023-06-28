from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from cloudinary.models import CloudinaryField


media_url=getattr(settings,'MEDIA_URL')
# Create your models here.
class Table(models.Model):
    name=models.CharField(max_length=200)
    table_No=models.IntegerField()
    def __str__(self) -> str:
        return str(self.name)


class MenuItem(models.Model):
    item_Group = (
    ("Alcohol", "Alchohol"),
    ("Cocktail ", "Cocktail"),
    ("Grills", "Grills"),
    ("Meals", "Meals"),

)
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    available_amount=models.IntegerField()
    group=models.CharField(choices=item_Group, max_length=250)
    image = CloudinaryField('image',blank=True,null=True)

    def __str__(self) -> str:
        return str(self.name)

class Order(models.Model):
    table=models.ForeignKey(Table,on_delete=models.CASCADE,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    total_price=models.IntegerField(default=0)
    processed=models.BooleanField(default=False)
    rejected=models.BooleanField(default=False)
    phone= models.CharField(max_length=11, blank=True, null=True)
    class Meta:
        ordering=['-created']
    def __str__(self) -> str:
        if self.table==None:
            return "Online Order"
        return str(self.table) + ' Order'

class OrderItem(models.Model):
    order_made=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_name',blank=True)
    product=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)



    def __str__(self) -> str:
        return str(self.order_made.table) +'Table Order'
