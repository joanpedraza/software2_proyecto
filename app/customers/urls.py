from django.urls import path
from .views import OrderListView, ProductListView, add_to_cart, create_order, remove_from_cart, update_cart_item, view_cart


urlpatterns = [
    path('list/', ProductListView.as_view(), name='products_list'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('update_cart_item/<int:product_id>/', update_cart_item, name='update_cart_item'),
    path('create_order/', create_order, name='create_order'),
    path('orders/', OrderListView.as_view(), name='order_list'),
]
