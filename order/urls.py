from django.urls import path,include
from .views import ListMenu,OrderView,OrderItemView



urlpatterns = [
    path('menu/',ListMenu.as_view()),
    path('order/',OrderView.as_view()),
    path('orderitem/',OrderItemView.as_view())
]