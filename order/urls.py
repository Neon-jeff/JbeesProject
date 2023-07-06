from django.urls import path,include
from .views import ListMenu,OrderView,OrderItemView,OrderUpdateView,MenuItemUpdateView



urlpatterns = [
    path('menu/',ListMenu.as_view()),
    path("menu/<pk>/", MenuItemUpdateView.as_view(), name="update-item"),
    path('order/',OrderView.as_view()),
    path('orderitem/',OrderItemView.as_view()),
    path("order/<pk>/", OrderUpdateView().as_view(), name="")
]
