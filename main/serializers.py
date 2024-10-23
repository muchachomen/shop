from rest_framework import serializers
from .models import Profile, Product, Categories, Orders, Cart
from django.contrib.auth.models import User


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
    image = serializers.ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = Product
        fields = ['id','name','description','cost', 'category', 'image', 'availability']


class categoryserialzer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name']


class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product']
