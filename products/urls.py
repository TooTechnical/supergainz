from django.urls import path
from django.conf import settings
from .views import product_detail
from . import views

urlpatterns = [
    path('<int:product_id>/', product_detail, name='product_detail'),
    path('free-download/<int:product_id>/', views.free_product_download, name='free_product_download'),
    path('', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout-cart/', views.checkout_cart, name='checkout_cart'),
]
