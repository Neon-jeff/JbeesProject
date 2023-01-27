from rest_framework import serializers
from .models import Order, MenuItem
import json

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem()
        ordering=['-id']
        fields='__all__'




class OrderSerializer(serializers.ModelSerializer):
    orderItem=MenuSerializer(many=True,read_only=True)
    class Meta:
        model=Order
        ordering=['-id']
        fields='__all__'

    
    def create(self, validated_data):
       
        dance_ids = []
        for dance in self.initial_data['orderItem']:
            print(dance)
            if 'id' not in dance:
                raise serializers.ValidationError({'detail': 'key error'})
            dance_ids.append(dance['id'])
            print

        new_order = Order.objects.create(**validated_data)
        
        if dance_ids:
            for dance_id in dance_ids:
                new_order.orderItem.add(dance_id)
                for i in range(len(dance_ids)-1):
                    new_order.orderItem[i]=self.initial_data['orderItem'][i]
        new_order.save()
        return new_order