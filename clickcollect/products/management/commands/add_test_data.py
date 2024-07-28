import logging

from django.core.management.base import BaseCommand

from products.models import Product
from stock.models import StockLocation, StockRecord
from customers.models import Customer

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Command(BaseCommand):
    """Management command to add test data"""

    help = "Add some test data"

    def handle(self, *args, **options):
        Customer.objects.create(name="Test Customer", email="test@test.com")

        product_1 = Product.objects.create(
            name="Test Product 1",
            unit_price=100.00,
            sku="ABC",
        )

        product_2 = Product.objects.create(
            name="Test Product 2",
            unit_price=80.00,
            sku="DEF",
        )

        product_3 = Product.objects.create(
            name="Test Product 3",
            unit_price=200.00,
            sku="GHI",
        )

        location = StockLocation.objects.create(location="København")

        StockRecord.objects.create(
            product=product_1, num_in_stock=99, location=location
        )
        StockRecord.objects.create(
            product=product_2, num_in_stock=99, location=location
        )
        StockRecord.objects.create(
            product=product_3, num_in_stock=99, location=location
        )

        self.stdout.write(self.style.SUCCESS("Successfully added test data"))
