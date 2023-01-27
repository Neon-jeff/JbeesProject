from django.db import models

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
    amount_ordered=models.IntegerField(default=0)
    selected=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.name)

class Order(models.Model):
    table=models.ForeignKey(Table,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    orderItem=models.ManyToManyField(MenuItem)
    total_price=models.IntegerField(default=0)
    def __str__(self) -> str:
        return str(self.table) + ' Order'