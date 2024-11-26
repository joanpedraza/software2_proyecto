from django.urls import path, include
from .views import home, exit, register

urlpatterns = [
    path('', home, name='home'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
]
