from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from .views import ProfileView, productList, categoryview, orderview, Cartview, Products
router = DefaultRouter()
router.register(r'products', Products)
urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', ProfileView.as_view()),
    path('product/', productList.as_view()),
    path('category/', categoryview.as_view()),
    path('order/', orderview.as_view()),
    path('cart/', Cartview.as_view()),
]
