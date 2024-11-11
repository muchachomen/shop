from django.contrib import admin
from .models import Product, Categories, CartItem, Order, Payment, Review
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(Payment)
admin.site.register(Review)

