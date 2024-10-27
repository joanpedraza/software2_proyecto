from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from app.store_admin.models import Product, Provider
from app.customers.models import Order

def admin_required(function=None, login_url='/accounts/login/'):
    return user_passes_test(lambda u: u.is_superuser, login_url=login_url)(function)

@admin_required
def dashboard(request):
    return render(request, 'store_admin/dashboard.html')

@admin_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        provider_id = request.POST['provider']

        provider = Provider.objects.get(id=provider_id)

        product = Product(name=name, description=description, price=price, quantity=quantity, provider=provider)
        product.save()

        return redirect('inventory')

    providers = Provider.objects.all()
    return render(request, 'store_admin/addProducts.html', {'providers': providers})

@admin_required
def inventory(request):
    products = Product.objects.all() 
    return render(request, 'store_admin/inventory.html', {'products': products})

@admin_required
def order_history(request):
    orders = Order.objects.all()  # Recupera todos los pedidos
    return render(request, 'store_admin/orders.html', {'orders': orders})

def exitAdmin(request):
    logout(request)
    return redirect('home')