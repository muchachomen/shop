from django.db import models

from main.models import Product


#
#
# Create your models here.

class ProductRedactor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

