from django.urls import path,include
from .views import ListMenu,OrderView



urlpatterns = [
    path('/menu/',ListMenu.as_view()),
    path('/order/',OrderView.as_view())
]