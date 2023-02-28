from django.db import models
from order.models import Table
# Create your models here.
class Messages(models.Model):
    table=models.OneToOneField(Table,on_delete=models.CASCADE)
    msgtext=models.TextField(max_length=3000)

    