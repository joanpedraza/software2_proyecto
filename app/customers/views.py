from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Product

class ProductListView(UserPassesTestMixin, ListView):
    model = Product
    template_name = 'customers/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def test_func(self):
        # Solo permite que los usuarios autenticados accedan a la tienda
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        from django.shortcuts import redirect
        print("NO HAY PERMISOS")
        return redirect('login')
