from rest_framework import serializers
from .models import Profile, Product, Categories, Order, CartItem, Review, Payment
from django.contrib.auth.models import User
import datetime

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['info', 'avatar']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['username', 'email', 'profile', 'password']



    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','name','description','cost', 'category', 'image', 'availability']


class categoryserialzer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'products', 'availability', 'user']

class OrderSerializer(serializers.ModelSerializer):
      class Meta:
        model = Order
        fields = ['id', 'product', 'method']






class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['name', 'status']


