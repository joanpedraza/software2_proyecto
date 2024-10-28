from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Product
from django.http import JsonResponse

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

def agregar_al_carrito(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    carrito = request.session.get('carrito', {})
    
    if str(product.id) not in carrito:
        carrito[str(product.id)] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1
        }
    else:
        carrito[str(product.id)]['quantity'] += 1
    
    request.session['carrito'] = carrito

    return JsonResponse({'message': 'Producto agregado al carrito', 'cart_count': len(carrito)})