from django.shortcuts import render
from rest_framework import generics
from .serializer import MenuSerializer,OrderSerializer
from .models import MenuItem,Order
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
        order=json.loads(request.body.decode('utf-8'))
        serializer=OrderSerializer(data=order)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        



