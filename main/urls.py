from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from .views import ProfileView, ProductList, Categoryview, Cartview, Products, DetailView, Orderlist, Reviews, Cartlist, PaymentView
router = DefaultRouter()
router.register(r'orders', Orderlist)
router.register(r'cart', Cartlist)
router.register(r'products', Products)


urlpatterns = [
    path('admins/', include(router.urls)),
    path('register/', ProfileView.as_view()),
    path('product/', ProductList.as_view()),
    path('category/', Categoryview.as_view()),
    path('cart/', Cartview.as_view()),
    path('products/<int:pk>/', DetailView.as_view(), name='product-detail'),
    path('review/', Reviews.as_view()),
    path('payments/', PaymentView.as_view())

]