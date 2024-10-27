from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def admin_required(function=None, login_url='/accounts/login/'):
    return user_passes_test(lambda u: u.is_superuser, login_url=login_url)(function)

@admin_required
def dashboard(request):
    return render(request, 'store_admin/dashboard.html')

@admin_required
def add_product(request):
    return render(request, 'store_admin/addProducts.html')

@admin_required
def inventory(request):
    return render(request, 'store_admin/inventory.html')

@admin_required
def order_history(request):
    return render(request, 'store_admin/orders.html')

def exitAdmin(request):
    logout(request)
    return redirect('home')