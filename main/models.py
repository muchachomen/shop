from decimal import Decimal
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework.pagination import PageNumberPagination


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=110)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    cost = models.IntegerField(default=0, validators=[MinValueValidator(0.01)])
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    image = models.ImageField()
    availability = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name



def update(self, instance, validated_data):
        setattr(instance.profile, "lang", validated_data.get("get_lang"))
        instance.save()
        return instance


class CartItem(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    availability = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)



class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class Payment(models.Model):
    name = models.TextField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.OneToOneField(CartItem, on_delete=models.CASCADE)
    method = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Reduce the availability of the product
        if self.product.products.availability >= self.product.availability:
            self.product.products.availability -= self.product.availability
            self.product.products.save()
        else:
            raise ValidationError("Not enough product availability for this order.")
        super().save(*args, **kwargs)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    order_history = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.user.username


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=500)
    rate = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])