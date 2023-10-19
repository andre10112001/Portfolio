from django.contrib import admin

from .models import User, Product, Purchase, BasketItem, ShoppingCart

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(BasketItem)
admin.site.register(ShoppingCart)
