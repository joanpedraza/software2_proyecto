from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from app.store_admin.models import Product, Provider
from app.customers.models import Order,Customer
import requests
from django.conf import settings
from datetime import datetime

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
        image = request.FILES['image']

        provider = Provider.objects.get(id=provider_id)

        product = Product(name=name, description=description, price=price, quantity=quantity, provider=provider, image=image)
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
    api_url = [f"{settings.API_BASE_URL}/customers/api/orders/", f"http://20.197.225.198:8080/api/pedido/list"]

    orders = []

    selected_customer = request.GET.get('customer')
    selected_store = request.GET.get('sucursal')    
    selected_start_date = request.GET.get('start_date')
    selected_end_date = request.GET.get('end_date')
    selected_min_price = request.GET.get('min_price')
    selected_max_price = request.GET.get('max_price')

    params = {
        'customer': selected_customer,
        'store': selected_store,        
        'start_date': selected_start_date,
        'end_date': selected_end_date,
        'min_price': selected_min_price,
        'max_price': selected_max_price,
    }

    for api in api_url:    

        try:
            response = requests.get(api, params=params)
            response.raise_for_status()  
            orders = orders + response.json()  
        except requests.RequestException as e:
            #orders = []  
            print(f"Error al conectar con la API: {e}")

        customers = Customer.objects.prefetch_related('user').all()

    return render(request, 'store_admin/orders.html', {
        'orders': orders,
        'customers': customers,
        'selected_store': selected_store,
        'selected_customer': selected_customer,
        'selected_start_date': selected_start_date,
        'selected_end_date': selected_end_date,
        'selected_min_price': selected_min_price,
        'selected_max_price': selected_max_price,
    })

def exitAdmin(request):
    logout(request)
    return redirect('home')