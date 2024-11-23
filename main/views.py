from rest_framework.generics import UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework import permissions, generics, status, serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import json
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .permissions import ISAdminBrothers
from .models import Product, Order, LargeResultsSetPagination, CartItem
from .serializers import UserSerializer, productSerializer, categoryserialzer, OrderSerializer, CartSerializer, Reviewserializer, PaymentSerializer


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
    permission_classes = [ISAdminBrothers]





class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data
        cart_item_id = data.get("product")
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            if cart_item.products.availability >= cart_item.availability:
                cart_item.products.availability -= cart_item.availability
                cart_item.products.save()
            else:
                return Response({"error": "Not enough availability for this product."},
                                status=status.HTTP_400_BAD_REQUEST)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item does not exist."}, status=status.HTTP_404_NOT_FOUND)






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
    permission_classes = [ISAdminBrothers]


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
    permission_classes = [AllowAny]

class Cartlist(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]



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

class PaymentView(generics.CreateAPIView):
    queryset = Product
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]