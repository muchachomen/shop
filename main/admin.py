from django.contrib import admin
from .models import Product, Categories, Cart, Orders
# Register your models here.
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Orders)
admin.site.register(Cart)