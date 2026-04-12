from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Молочные продукты')

        products = [
            {'name': 'Молоко', 'price':'50', 'category': category},
            {'name': 'Сливки', 'price':'70', 'category': category},
        ]

        for product_category in products:
            product, created = Product.objects.get_or_create(**product_category)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.name}'))
