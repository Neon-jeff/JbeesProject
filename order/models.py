from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.contrib.sites.models import Site

domain = Site.objects.get(id=5).domain


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
    image=models.ImageField( upload_to='images/',null=True,blank=True)
    image_url=models.URLField(max_length=200,null=True,blank=True)
    group=models.CharField(choices=item_Group, max_length=250)

    def save(self,*args,**kwargs):
        if self.image:
            self.image_url=f'{domain}{media_url}{self.image}'
        super(MenuItem, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.name)

class Order(models.Model):
    table=models.ForeignKey(Table,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    total_price=models.IntegerField(default=0)
    processed=models.BooleanField(default=False)
    rejected=models.BooleanField(default=False)

    class Meta:
        ordering=['-created']
    def __str__(self) -> str:
        return str(self.table) + ' Order'

class OrderItem(models.Model):
    order_made=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_name',blank=True)
    product=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)



    def __str__(self) -> str:
        return str(self.order_made.table) +'Table Order'
