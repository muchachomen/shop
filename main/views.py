import requests
import self
import stripe
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .permissions import ISAdminBrothers
from .models import Product, Order, LargeResultsSetPagination, CartItem
from .serializers import UserSerializer, productSerializer, categoryserialzer, Orderserializer, CartSerializer, Reviewserializer


# Create your views here.



class ProfileView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        print(request.data)
        data = request.data
        reg_serializer = UserSerializer(data=data)
        if reg_serializer.is_valid():
            password = reg_serializer.validated_data.get('password')
            reg_serializer.validated_data['password'] = make_password(password)
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Categoryview(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = categoryserialzer
    permission_classes = [AllowAny]

class Orderview(generics.CreateAPIView):
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


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = [AllowAny]

class Orderlist(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = Orderserializer
    permission_classes = [AllowAny]

class Reviews(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Reviewserializer

class Cartlist(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]




