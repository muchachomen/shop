from django.contrib import admin
from .models import Product, Categories, CartItem, Orders, Payment, Review
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Orders)
admin.site.register(CartItem)
admin.site.register(Payment)
admin.site.register(Review)

