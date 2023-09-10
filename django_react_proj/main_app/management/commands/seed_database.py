from django.core.management.base import BaseCommand
from main_app.models import Categories, Product, Customer, SaleOrder, SaleOrderLine, Vendor, PurchaseOrder, PurchaseOrderLine
import random
from faker import Faker

# Create an instance of the Faker library to generate fake data
fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **options):
        category1 = Categories.objects.get(id=1)
        category2 = Categories.objects.get(id=2)
        customer1 = Customer.objects.get(id=1)
        customer2 = Customer.objects.get(id=2)
        # Your seeding logic here
        categories = [
            Categories(name='Category 1', image='category1.jpg', number=1),
            Categories(name='Category 2', image='category2.jpg', number=2),
        ]
        Categories.objects.bulk_create(categories)

        products = [
            Product(name='Product 1', purchaseCost=10.99, salePrice=19.99, image='product1.jpg', categoryId=category1),
            Product(name='Product 2', purchaseCost=15.99, salePrice=29.99, image='product2.jpg', categoryId=category2),
        ]
        Product.objects.bulk_create(products)

        customers = [
            Customer(name='Customer 1',phone='123-456-7890',email='customer1@example.com'),
            Customer(name='Customer 2',phone='987-654-3210',email='customer2@example.com'),
        ]
        Customer.objects.bulk_create(customers)

        sale_orders = [
            SaleOrder(saleDate='2023-09-15',saleNote='Order 1',confirmed=True,customerId=customer1),
            SaleOrder(saleDate='2023-09-16',saleNote='Order 2',confirmed=False,customerId=customer2),
        ]
        SaleOrder.objects.bulk_create(sale_orders)

        # sale_order_lines = [
        #     SaleOrderLine(quantity=3,saleId=SaleOrder.objects.get(id=1),productId=Product.objects.get(id=3),),
        #     SaleOrderLine(quantity=2,saleId=SaleOrder.objects.get(id=2),productId=Product.objects.get(id=4),),
        # ]
        # SaleOrderLine.objects.bulk_create(sale_order_lines)

        vendors = [
                Vendor(name='Vendor 1',phone='111-222-3333',email='vendor1@example.com',),
                Vendor(name='Vendor 2',phone='444-555-6666',email='vendor2@example.com',),
        ]
        Vendor.objects.bulk_create(vendors)

        purchase_orders = [
                PurchaseOrder(saleDate='2023-09-10',saleNote='Purchase 1',confirmed=True,vendorId=Vendor.objects.get(id=1),),
                PurchaseOrder(saleDate='2023-09-12',saleNote='Purchase 2',confirmed=False,vendorId=Vendor.objects.get(id=2),),
        ]
        PurchaseOrder.objects.bulk_create(purchase_orders)

        purchase_order_lines = [
            PurchaseOrderLine(quantity=5,purchaseId=PurchaseOrder.objects.get(id=1),productId=Product.objects.get(id=3),),
            PurchaseOrderLine(quantity=4,purchaseId=PurchaseOrder.objects.get(id=2),productId=Product.objects.get(id=4),),
        ]
        PurchaseOrderLine.objects.bulk_create(purchase_order_lines)
        self.stdout.write(self.style.SUCCESS('Database seeding complete'))
