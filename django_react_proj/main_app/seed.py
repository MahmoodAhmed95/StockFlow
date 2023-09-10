# Import necessary modules
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stockflow.settings")

# Initialize Django
django.setup()
from faker import Faker
import random
from models import Categories, Product, Customer, SaleOrder, SaleOrderLine, Vendor, PurchaseOrder, PurchaseOrderLine
from django.db import transaction

# Create an instance of the Faker library
fake = Faker()

# Define the seed_data function
def seed_data():
    with transaction.atomic():
        # Create categories
        categories = []
        for _ in range(5):
            category = Categories.objects.create(
                name=fake.word(),
                image=fake.image_url(),
                number=random.randint(1, 100)
            )
            categories.append(category)

        # Create products
        products = []
        for _ in range(20):
            product = Product.objects.create(
                name=fake.unique.word(),
                purchaseCost=random.uniform(10, 1000),
                salePrice=random.uniform(20, 2000),
                image=fake.image_url(),
                categoryId=random.choice(categories)
            )
            products.append(product)

        # Create customers
        customers = []
        for _ in range(10):
            customer = Customer.objects.create(
                name=fake.name(),
                phone=fake.phone_number(),
                email=fake.email()
            )
            customers.append(customer)

        # Create sale orders
        for _ in range(30):
            sale_order = SaleOrder.objects.create(
                saleDate=fake.date_between(start_date='-30d', end_date='today'),
                saleNote=fake.sentence(),
                confirmed=random.choice([True, False]),
                customerId=random.choice(customers)
            )

            # Create sale order lines
            for _ in range(random.randint(1, 5)):
                SaleOrderLine.objects.create(
                    quantity=random.randint(1, 10),
                    saleId=sale_order,
                    productId=random.choice(products)
                )

        # Create vendors
        vendors = []
        for _ in range(5):
            vendor = Vendor.objects.create(
                name=fake.company(),
                phone=fake.phone_number(),
                email=fake.email()
            )
            vendors.append(vendor)

        # Create purchase orders
        for _ in range(20):
            purchase_order = PurchaseOrder.objects.create(
                saleDate=fake.date_between(start_date='-30d', end_date='today'),
                saleNote=fake.sentence(),
                confirmed=random.choice([True, False]),
                vendorId=random.choice(vendors)
            )

            # Create purchase order lines
            for _ in range(random.randint(1, 5)):
                PurchaseOrderLine.objects.create(
                    quantity=random.randint(1, 10),
                    purchaseId=purchase_order,
                    productId=random.choice(products)
                )

# Execute the seed_data function when this script is run
if __name__ == '__main__':
    seed_data()
