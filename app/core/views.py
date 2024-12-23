from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomRegisterForm
from django.contrib.auth import authenticate, login
from app.customers.models import Customer

# Create your views here.
def home(request):
    return redirect('products_list')

def exit(request):
    logout(request)
    return redirect('products_list')

def register(request):
    data = {
        'form': CustomRegisterForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomRegisterForm(data=request.POST)
        
        if user_creation_form.is_valid():
            customer = user_creation_form.save()
            Customer.objects.create(user=customer)

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])    
            login(request, user)
            
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)


@login_required
def custom_login_redirect(request):
    if request.user.is_superuser:
        return redirect('dashboard')  
    return redirect('home') 