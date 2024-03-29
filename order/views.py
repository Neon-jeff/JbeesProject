from django.shortcuts import render
from rest_framework import generics
from .serializer import MenuSerializer,OrderSerializer,OrderItemSerializer
from .models import MenuItem,Order,OrderItem,Table
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
import json
# Create your views here.

class ListMenu(APIView):
    parser_classes=[MultiPartParser,FormParser]
    def get(self,request):
        menu=MenuItem.objects.all()
        serializer=MenuSerializer(menu,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer=MenuSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
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
        print(order)
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

class MenuItemUpdateView(APIView):
    parser_classes=[MultiPartParser,FormParser]
    def get_object(self, pk):
        return MenuItem.objects.get(pk=pk)

    def patch(self, request, pk,format=None):
        menu_object = self.get_object(pk)
        serializer = MenuSerializer(menu_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class OrderItemView(generics.ListCreateAPIView):
    serializer_class=OrderItemSerializer
    queryset=OrderItem.objects.all()




