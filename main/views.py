import requests
import self
import stripe
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny
from requests import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import ISAdminBrothers
from .models import Product, Orders
from .serializers import UserSerializer, productSerializer, categoryserialzer, Orderserializer, CartSerializer, Reviewserializer


# Create your views here.



class ProfileView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class categoryview(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = categoryserialzer
    permission_classes = [ISAdminBrothers]

class orderview(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Orderserializer
    permission_classes = [AllowAny]

class Cartview(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]
class Products(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permission_classes = [AllowAny]

class DetailView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permission_classes = [AllowAny]

class productList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permission_classes = [AllowAny]

class Orderlist(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = Orderserializer
    permission_classes = [ISAdminBrothers]

class Reviews(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Reviewserializer
    permission_classes = [AllowAny]



