from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class RegisterView(TemplateView):
    template_name = 'register.html'

class ProductListView(TemplateView):
    template_name = 'products.html'

class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'

class CartView(TemplateView):
    template_name = 'cart.html'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'

class AddressView(TemplateView):
    template_name = 'address.html'

class MyOrdersView(TemplateView):
    template_name = 'orders.html'

class AdminDashboardView(TemplateView):
    template_name = 'admin_dashboard.html'

class AddProductView(TemplateView):
    template_name = 'add_product.html'

class AdminOrderView(TemplateView):
    template_name = 'admin_orders.html'
