
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('products', views.products , name='products'),
    path('addcomment/<str:id>', views.addcomment , name='addcomment'),
    path('details/<str:pk>', views.details , name='details'),
    
]