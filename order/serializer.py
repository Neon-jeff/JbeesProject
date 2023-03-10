from rest_framework import serializers
from .models import Order, MenuItem,OrderItem,Table
import json

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        ordering=['-id']
        fields='__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product=MenuSerializer()
    class Meta:
        model=OrderItem
        fields='__all__'
        ordering=['-id']


class OrderSerializer(serializers.ModelSerializer):
    # orderItem=MenuSerializer(many=True,read_only=True)
    order_name=OrderItemSerializer(many=True,allow_null=True,required=False)
    class Meta:
        model=Order
        ordering=['-id']
        fields='__all__'
        
    
    def create(self, validated_data):
        orders=self.initial_data['order_item']
        # create order instance
        orderInstance=Order.objects.create(
            table=Table.objects.get(id=self.initial_data['table']),
            total_price=self.initial_data['total_price']
        )
        # create order instance related items 
        for i in orders:
            OrderItem.objects.create(
            amount=i['amount'],
            product=MenuItem.objects.get(id=i['product']['id']),
            order_made=orderInstance
            )
        #  attach order items to related instance  
        orderInstance.order_name.set=OrderItem.objects.filter(order_made=orderInstance)
        # update serializer field
        self.order_name=orderInstance.order_name
        orderInstance.save()
        return orderInstance
   
       

