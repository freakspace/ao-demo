import logging

from django.core.management.base import BaseCommand

from products.models import Product
from stock.models import StockLocation, StockRecord

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Command(BaseCommand):
    help = "Add some test data"

    def handle(self, *args, **options):

        product = Product.objects.create(
            name="Test Product 1",
            unit_price=100.00,
            sku="GG_ABC",
        )

        location = StockLocation.objects.create(location="København")

        StockRecord.objects.create(product=product, num_in_stock=99, location=location)

        self.stdout.write(self.style.SUCCESS("Successfully ran automations"))
