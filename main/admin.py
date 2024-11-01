from django.contrib import admin
from .models import Product, Categories, Cart, Orders, Payment, Review
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Orders)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Review)

