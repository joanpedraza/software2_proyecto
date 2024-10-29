from django.contrib import admin
from .models import Customer, Order, ProductOrder, Cart, CartItem

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ProductOrder)
admin.site.register(Cart)
admin.site.register(CartItem)
