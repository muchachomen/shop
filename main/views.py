from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from requests import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Product
from .serializers import UserSerializer, productSerializer, categoryserialzer, Orderserializer, CartSerializer
# Create your views here.


class MySecureView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(data={"message": "Это защищенное представление!"})



class ProfileView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class productList(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permission_classes = [AllowAny]

class categoryview(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = categoryserialzer
    permission_classes = [AllowAny]

class orderview(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Orderserializer
    permission_classes = [AllowAny]

class Cartview(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

