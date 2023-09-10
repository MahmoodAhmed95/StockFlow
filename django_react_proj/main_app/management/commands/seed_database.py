# myapp/management/commands/seed_database.py
from django.core.management.base import BaseCommand
from main_app.models import Categories, Product  # Import your models

class Command(BaseCommand):
    help = 'Seed the database with initial data'
    def handle(self, *args, **options):
        category1 = Categories.objects.get(id=1)
        category2 = Categories.objects.get(id=2)
        # Your seeding logic here
        categories = [
            Categories(name='Category 1', image='category1.jpg', number=1),
            Categories(name='Category 2', image='category2.jpg', number=2),
            # Add more instances as needed
        ]
        Categories.objects.bulk_create(categories)

        products = [
            Product(name='Product 1', purchaseCost=10.99, salePrice=19.99, image='product1.jpg', categoryId=category1),
            Product(name='Product 2', purchaseCost=15.99, salePrice=29.99, image='product2.jpg', categoryId=category2),
            # Add more instances as needed
        ]
        Product.objects.bulk_create(products)

        self.stdout.write(self.style.SUCCESS('Database seeding complete'))
