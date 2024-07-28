from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(_("Product name"), max_length=255)
    unit_price = models.DecimalField(
        _("Unit Price"),
        decimal_places=2,
        max_digits=12,
        blank=True,
        null=True,
    )
    sku = models.CharField(_("Product number"), max_length=255)

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    pass


class ProductOptionValue(models.Model):
    pass
