from django.urls import path,include
from .views import ListMenu,OrderView,OrderItemView,OrderUpdateView



urlpatterns = [
    path('menu/',ListMenu.as_view()),
    path('order/',OrderView.as_view()),
    path('orderitem/',OrderItemView.as_view()),
    path("order/<pk>/", OrderUpdateView().as_view(), name="")
]
