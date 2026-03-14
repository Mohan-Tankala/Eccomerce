import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from ecommerce.models import User, Category

# Create Superuser/Admin
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword123', role='admin')
    print("Admin user created.")
else:
    print("Admin user already exists.")

# Create Categories
categories = [
    ('Electronics', 'Gadgets and hardware'),
    ('Fashion', 'Clothing and accessories'),
    ('Home & Kitchen', 'Home decor and appliances')
]

for name, desc in categories:
    obj, created = Category.objects.get_or_create(name=name, defaults={'description': desc})
    if created:
        print(f"Category '{name}' created.")

print("Setup complete.")
