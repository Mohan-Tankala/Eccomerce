from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView, LoginView, LogoutView, 
    CategoryListView, ProductListView, ProductDetailView, AdminProductView,
    CartView, AddToCartView, UpdateCartItemView, RemoveFromCartView,
    AddressViewSet, CreateOrderView, MyOrdersView, 
    AdminOrderListView, AdminOrderUpdateView
)

urlpatterns = [
    # Auth
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Products & Categories
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('admin/products/', AdminProductView.as_view(), name='admin-product-create'),
    path('admin/products/<int:pk>/', AdminProductView.as_view(), name='admin-product-detail'),
    
    # Cart
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='cart-add'),
    path('cart/items/<int:pk>/', UpdateCartItemView.as_view(), name='cart-update'),
    path('cart/items/<int:pk>/delete/', RemoveFromCartView.as_view(), name='cart-remove'),
    
    # Orders & Addresses
    path('addresses/', AddressViewSet.as_view(), name='address-list'),
    path('orders/', MyOrdersView.as_view(), name='my-orders'),
    path('orders/create/', CreateOrderView.as_view(), name='order-create'),
    path('admin/orders/', AdminOrderListView.as_view(), name='admin-orders'),
    path('admin/orders/<int:pk>/', AdminOrderUpdateView.as_view(), name='admin-order-update'),
]
