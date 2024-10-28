from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ProductRedactor
class Adminregserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'groups']



class ProductRed(serializers.ModelSerializer):
    class Meta:
        model = ProductRedactor
        fields = ['product']
