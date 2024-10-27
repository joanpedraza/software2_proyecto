from django.urls import path
from .views import dashboard, add_product, inventory, order_history

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add_product/', add_product, name='add_product'),
    path('inventory/', inventory, name='inventory'),
    path('order_history/', order_history, name='order_history'),
]