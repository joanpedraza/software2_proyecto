from rest_framework import serializers
from app.customers.models import Order, ProductOrder

class ProductOrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = ProductOrder
        fields = ['product_name', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    products = ProductOrderSerializer(source='productorder_set', many=True, read_only=True)
    customer_name = serializers.CharField(source='customer.user.get_full_name', read_only=True)
    status = serializers.CharField(default='Registrado')
    store = serializers.CharField(default='3A-STORE')

    class Meta:
        model = Order
        fields = ['id', 'date', 'status', 'store', 'customer_name', 'total_price', 'products']