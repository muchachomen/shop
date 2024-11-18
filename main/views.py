
from rest_framework.generics import UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework import permissions, generics, status, serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import json
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .permissions import ISAdminBrothers
from .models import Product, Order, LargeResultsSetPagination, CartItem
from .serializers import UserSerializer, productSerializer, categoryserialzer, OrderSerializer, CartSerializer, Reviewserializer, ProductsUpdateSerializer


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
    serializer_class = OrderSerializer
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
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

class Reviews(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Reviewserializer

class Cartlist(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]


class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsUpdateSerializer
    permission_classes = [AllowAny]
    lookup_field = 'name'
    lookup_url_kwarg = 'name'

class ProcessOrderView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        order_id = request.data.get("order_id")
        try:
            order = Order.objects.get(id=order_id)
            order.process_order()
            return Response({"status": "Order processed successfully"})
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)



class CreateOrderView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            try:
                order = serializer.save(is_processed=True)  # Создаём заказ и обрабатываем его
                return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)