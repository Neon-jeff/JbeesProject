from rest_framework import serializers
from .models import Order, MenuItem,OrderItem,Table
import json
from drf_writable_nested import WritableNestedModelSerializer

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        ordering=['-id']
        fields='__all__'
    def create(self, validated_data):
        return MenuItem.objects.create(**validated_data)

class OrderItemSerializer(serializers.ModelSerializer):
    product=MenuSerializer()
    class Meta:
        model=OrderItem
        fields='__all__'
        ordering=['-id']


class OrderSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    # orderItem=MenuSerializer(many=True,read_only=True)
    order_name=OrderItemSerializer(many=True,allow_null=True,required=False,read_only=True)
    class Meta:
        model=Order
        ordering=['-id']
        fields='__all__'


    def create(self, validated_data):
        orders=self.initial_data['order_item']
        # create order instance
        orderInstance=Order.objects.create(
            table=Table.objects.get(table_No=self.initial_data['table']),
            total_price=self.initial_data['total_price'],
            phone=self.initial_data['phone']
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

        # def update(self, instance, validated_data):
        #     instance=Order.objects.get(id=validated_data['id'])
        #     instance.processed=validated_data['processed']
        #     instance.rejected=validated_data['rejected']
        #     instance.save()
        #     return instance

# i had to install pip install drf-writable-nested this package to allow me update nested elements
