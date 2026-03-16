import os
import django
from django.core.files import File

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from ecommerce.models import Product

def upload_images():
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME')
    if not cloud_name:
        print("\n[!] Error: Cloudinary credentials not found in environment variables.")
        print("    Please set CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, and CLOUDINARY_API_SECRET in your .env or Render dashboard.\n")
        return

    products = Product.objects.all()
    print(f"\n[*] Found {products.count()} products. Checking for images to upload...")

    success_count = 0
    fail_count = 0
    skipped_count = 0

    for product in products:
        if not product.image:
            print(f"[-] Skipping '{product.name}': No image assigned.")
            skipped_count += 1
            continue
        
        # Check if the image is already on Cloudinary
        image_url = str(product.image.url)
        if 'cloudinary.com' in image_url:
            print(f"[-] Skipping '{product.name}': Image already on Cloudinary ({image_url}).")
            skipped_count += 1
            continue

        # Get local path
        try:
            local_path = product.image.path
            if os.path.exists(local_path):
                print(f"[+] Uploading '{product.name}' image to Cloudinary...")
                with open(local_path, 'rb') as f:
                    # Saving to the field with same name will trigger the storage backend (Cloudinary)
                    product.image.save(os.path.basename(local_path), File(f), save=True)
                print(f"    Successfully uploaded: {product.image.url}")
                success_count += 1
            else:
                print(f"[!] Warning: Local file for '{product.name}' not found at {local_path}")
                fail_count += 1
        except Exception as e:
            print(f"[!] Failed to upload '{product.name}': {str(e)}")
            fail_count += 1

    print(f"\n[*] Upload process complete:")
    print(f"    Success: {success_count}")
    print(f"    Failed:  {fail_count}")
    print(f"    Skipped: {skipped_count}\n")

if __name__ == "__main__":
    upload_images()
