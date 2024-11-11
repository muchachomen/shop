from rest_framework import serializers
from .models import Profile, Product, Categories, Order, CartItem, Review
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

    def cost(self, value):
        cost = ['cost']
        if cost not in  0:
            print("all right")
        else:
            raise serializers.ValidationError("wrong number")
        return value

class categoryserialzer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name']


class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'



class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'




