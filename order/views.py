from django.shortcuts import render
from rest_framework import generics
from .serializer import MenuSerializer,OrderSerializer,OrderItemSerializer
from .models import MenuItem,Order,OrderItem
from rest_framework.response import Response
from rest_framework.views import APIView
import json
# Create your views here.

class ListMenu(generics.ListAPIView):
    serializer_class=MenuSerializer
    queryset=MenuItem.objects.all()

class OrderView(APIView):
    def get(self,request):
        order=Order.objects.all()
        serializer=OrderSerializer(order,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        order=json.loads(request.body)
        serializer=OrderSerializer(data=order)  
        
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data) 
            # print(serializer.instance)
            serializer.save()
            return Response(serializer.data)
            

class OrderItemView(generics.ListCreateAPIView):
    serializer_class=OrderItemSerializer
    queryset=OrderItem.objects.all()
        



