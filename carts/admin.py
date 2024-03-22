from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'is_active']

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)