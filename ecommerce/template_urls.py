from django.urls import path
from .template_views import (
    HomeView, LoginView, RegisterView, ProductListView, ProductDetailView,
    CartView, CheckoutView, AddressView, MyOrdersView,
    AdminDashboardView, AddProductView, AdminOrderView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('register/', RegisterView.as_view(), name='register_page'),
    path('products/', ProductListView.as_view(), name='products_page'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail_page'),
    path('cart/', CartView.as_view(), name='cart_page'),
    path('checkout/', CheckoutView.as_view(), name='checkout_page'),
    path('address/', AddressView.as_view(), name='address_page'),
    path('orders/', MyOrdersView.as_view(), name='orders_page'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard_page'),
    path('admin/add-product/', AddProductView.as_view(), name='add_product_page'),
    path('admin/orders/', AdminOrderView.as_view(), name='admin_orders_page'),
]
