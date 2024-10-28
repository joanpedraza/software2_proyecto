from django.urls import path
from .views import ProductListView, agregar_al_carrito


urlpatterns = [
    path('list/', ProductListView.as_view(), name='products-list'),
    path('agregar_al_carrito/<int:product_id>/', agregar_al_carrito, name='agregar_al_carrito'),
]
