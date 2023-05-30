from django.shortcuts import render
from rest_framework import generics
from .serializer import MenuSerializer,OrderSerializer,OrderItemSerializer
from .models import MenuItem,Order,OrderItem
from rest_framework.response import Response
from rest_framework.views import APIView
import json
# Create your views here.

class ListMenu(APIView):
    menu=MenuItem.objects.all()
    def get(self,request):
        serializer=MenuSerializer(self.menu,many=True)
        return Response(serializer.data)
    def post(self,request):
        menu=json.loads(request.body)
        serializer=MenuSerializer(data=menu)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data)
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
    # def put(self,request):
    #     order=json.loads(request.body)
    #     serializer=OrderSerializer(data=order)

    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)

class OrderUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()

class OrderItemView(generics.ListCreateAPIView):
    serializer_class=OrderItemSerializer
    queryset=OrderItem.objects.all()




