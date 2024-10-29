from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from app.store_admin.models import Product, Provider
from app.customers.models import Order,Customer

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
    orders = Order.objects.prefetch_related('productorder_set__product','customer','supervisor').all()
    customers = Customer.objects.prefetch_related('user').all()

    customer_id = request.GET.get('customer')
    date = request.GET.get('date')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if customer_id:
        orders = orders.filter(customer_id=customer_id)
    if date:
        orders = orders.filter(date=date)
    if min_price:
        orders = orders.filter(total_price__gte=min_price)
    if max_price:
        orders = orders.filter(total_price__lte=max_price)
        

    return render(request, 'store_admin/orders.html', {'orders': orders, 'customers': customers})

def exitAdmin(request):
    logout(request)
    return redirect('home')