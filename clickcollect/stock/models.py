from django.db import models

from django.utils.translation import gettext as _

from products.models import Product


class StockLocation(models.Model):
    location = models.CharField(_("Location"), max_length=255)

    def __str__(self):
        return self.location


class StockRecord(models.Model):
    product = models.ForeignKey(
        Product, related_name="stock_records", on_delete=models.CASCADE
    )
    num_in_stock = models.PositiveIntegerField(_("Number in stock"), default=0)
    location = models.ForeignKey(
        StockLocation,
        related_name="stock_locations",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return _("{} - {} in stock").format(self.product, self.num_in_stock)
