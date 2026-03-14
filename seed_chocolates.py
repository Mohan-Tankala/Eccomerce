import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from ecommerce.models import Category, Product

# Clear existing categories and products (optional, but good for a fresh seed)
# Product.objects.all().delete()
# Category.objects.all().delete()

# Create Chocolate Categories
categories = [
    ('Dark Chocolates', 'Rich, bitter, and luxurious dark chocolates with high cocoa content.'),
    ('Milk Chocolates', 'Smooth, creamy, and classic milk chocolate delights.'),
    ('White Chocolates', 'Sweet and velvety white chocolate treats.'),
    ('Truffles & Pralines', 'Exquisite handcrafted truffles and pralines with gourmet fillings.'),
    ('Assorted Gift Boxes', 'Perfectly curated boxes for any occasion.')
]

category_objs = {}
for name, desc in categories:
    obj, created = Category.objects.get_or_create(name=name, defaults={'description': desc})
    category_objs[name] = obj
    if created:
        print(f"Category '{name}' created.")

# Add Sample Products
sample_products = [
    {
        'name': '70% Dark Origin bar',
        'description': 'Intense dark chocolate made from single-origin Ghanaian cocoa beans.',
        'price': 8.99,
        'category': category_objs['Dark Chocolates'],
        'stock': 50
    },
    {
        'name': 'Classic Milk Silk',
        'description': 'Velvety smooth milk chocolate that melts in your mouth.',
        'price': 6.50,
        'category': category_objs['Milk Chocolates'],
        'stock': 100
    },
    {
        'name': 'Hazelnut Praline Truffle',
        'description': 'Hand-rolled truffles filled with roasted hazelnut praline.',
        'price': 12.99,
        'category': category_objs['Truffles & Pralines'],
        'stock': 30
    },
    {
        'name': 'Signature Signature Box',
        'description': 'A collection of our 12 finest artisanal chocolates.',
        'price': 24.99,
        'category': category_objs['Assorted Gift Boxes'],
        'stock': 20
    }
]

for p_data in sample_products:
    if not Product.objects.filter(name=p_data['name']).exists():
        Product.objects.create(
            name=p_data['name'],
            description=p_data['description'],
            price=p_data['price'],
            category=p_data['category'],
            stock_quantity=p_data['stock']
        )
        print(f"Product '{p_data['name']}' created.")

print("Chocolate seeding complete.")
