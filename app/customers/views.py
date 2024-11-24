from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Cart, CartItem, Customer, Order, Product, ProductOrder, Supervisor
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializer import OrderSerializer,ProductOrderSerializer

class ProductListView(UserPassesTestMixin, ListView):
    model = Product
    template_name = 'customers/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def test_func(self):
        # Solo permite que los usuarios autenticados accedan a la tienda
        return True #self.request.user.is_authenticated

    def handle_no_permission(self):
        from django.shortcuts import redirect
        print("NO HAY PERMISOS")
        return redirect('login')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return JsonResponse({"message": "Producto agregado al carrito"})

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    items = [
        {
            "product_id": item.product.id,
            "name": item.product.name,
            "quantity": item.quantity,
            "total_price_currency": str(item.total_price().currency),
            "total_price_amount": str(round(item.total_price().amount,0))
        }
        for item in cart.items.all()
    ]

    return JsonResponse({
        "items": items,
        "totals_amount": str(round(cart.total_price().amount,0)),
        "totals_currency": str(cart.total_price().currency) if cart.total_price().currency else "COP",
    })

def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    return JsonResponse({"message": "Producto eliminado del carrito"})

def update_cart_item(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    quantity_change = int(request.GET.get("quantity", 1))
    new_quantity = cart_item.quantity + quantity_change

    if new_quantity <= 0:
        cart_item.delete()
        return JsonResponse({"message": "Cantidad actualizada en el carrito"})

    cart_item.quantity = new_quantity
    cart_item.save()
 
    return JsonResponse({"message": "Cantidad actualizada en el carrito"})

@login_required
def create_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        return JsonResponse({"message": "El carrito está vacío"}, status=400)

    supervisor = Supervisor.objects.all().first()
    customer = Customer.objects.filter(user=request.user).first()

    total_quantity = sum(item.quantity for item in cart.items.all())
    total_price = cart.total_price()

    order = Order.objects.create(
        customer=customer,
        supervisor=supervisor,
        total_quantity=total_quantity,
        total_price=total_price.amount,
        date=timezone.now().date()
    )

    for item in cart.items.all():
        ProductOrder.objects.create(
            product=item.product,
            order=order,
            quantity=item.quantity
        )

    cart.items.all().delete()

    return JsonResponse({"message": "Pedido creado exitosamente", "order_id": order.id, "redirect_url": reverse('order_list')})
class OrderListView(UserPassesTestMixin, ListView):
    model = Order
    template_name = 'customers/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.customer)

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        from django.shortcuts import redirect
        return redirect('login')
    

# Serializers
class OrderAPIView(APIView):
    def get(self, request):
        orders = Order.objects.prefetch_related('productorder_set__product', 'customer__user').all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)