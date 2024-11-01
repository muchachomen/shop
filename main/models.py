from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Categories(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    cost = models.IntegerField(validators=[MinValueValidator(0.01)])
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    image = models.ImageField()
    availability = models.IntegerField()

    def __str__(self):
        return self.name



class Cart(models.Model):
    list = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)







class Payment(models.Model):
    name = models.TextField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    info = models.TextField()
    contacts = models.CharField(max_length=19)
    method = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    order_history = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=500)
    rate = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])





