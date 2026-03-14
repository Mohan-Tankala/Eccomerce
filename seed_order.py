import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from ecommerce.models import User, Product, Address, Order, OrderItem

def seed_order():
    admin = User.objects.get(username='admin')
    product = Product.objects.first()
    
    if not product:
        print("No products found. Please seed products first.")
        return

    address, created = Address.objects.get_or_create(
        user=admin,
        full_name='Admin Test',
        phone='1234567890',
        street='123 Admin Lane',
        city='System',
        state='Digital',
        zip_code='000000',
        country='Cloud'
    )
    
    order = Order.objects.create(
        user=admin,
        address=address,
        total_amount=product.price,
        status='pending'
    )
    
    OrderItem.objects.create(
        order=order,
        product=product,
        quantity=1,
        price=product.price
    )
    
    print(f"Test order #{order.id} created for admin.")

if __name__ == '__main__':
    seed_order()
