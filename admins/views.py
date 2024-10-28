from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from main.models import Product
from .serializers import Adminregserializer, ProductRed
from rest_framework import serializers, generics, viewsets, status

# Create your views here.

class AdminUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Adminregserializer
    permission_classes = [AllowAny]


class ProductredView(generics.CreateAPIView):
    queryset = Product.objects.all
    serializer_class = ProductRed
    permission_classes = [AllowAny]


