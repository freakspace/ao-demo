from django.db import models

from django.utils.translation import gettext as _

from stock.models import StockLocation
from products.models import Product
from customers.models import Customer

ORDERSTATUS = (
    ("On hold", _("On hold")),
    ("Pending", _("Pending")),
    ("Ready", _("Ready")),
    ("Collected", _("Collected")),
)


class Order(models.Model):

    class Meta:
        ordering = ["-created"]

    customer = models.ForeignKey(
        Customer,
        related_name="orders",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    created = models.DateTimeField(auto_now_add=True)

    total_excl_tax = models.DecimalField(
        _("Order total (excl. tax)"), decimal_places=2, max_digits=12
    )

    location = models.ForeignKey(
        StockLocation,
        null=True,
        blank=True,
        verbose_name=_("Stock location for customer pick-up"),
        on_delete=models.SET_NULL,
    )

    order_status = models.CharField(
        _("Order Status"),
        help_text=_("Status of the order"),
        choices=ORDERSTATUS,
        max_length=255,
        default="On hold",
    )

    def __str__(self):
        return f"Order ID {self.pk} ({self.customer} - {self.created})"

    def is_ready_for_pickup(self):
        """Check if all order lines are received"""
        return all(self.lines.values_list("received", flat=True))

    def deduct_stock(self):
        """Deduct stock from the location"""
        for line in self.lines.filter(received=True):
            record = line.product.stock_records.get(location=self.location)
            record.num_in_stock -= line.quantity
            record.save()

    def log_action(self, message: str):
        OrderLog.objects.create(order=self, message=message)


class OrderLine(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="lines", verbose_name=_("Order")
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Product"),
    )

    title = models.CharField(_("Product title"), max_length=255)

    quantity = models.PositiveIntegerField(_("Quantity"), default=1)

    unit_price = models.DecimalField(
        _("Unit Price"),
        decimal_places=2,
        max_digits=12,
        blank=True,
        null=True,
        default=0,
    )

    received = models.BooleanField(_("Received"), default=False)

    def __str__(self):
        return f"Orderline ID {self.pk} ({self.quantity}x {self.title})"

    def total(self):
        """Return the total price for the line"""
        return self.quantity * self.unit_price

    def in_stock(self):
        """Return the number of items in stock for the product"""
        return self.product.stock_records.get(location=self.order.location).num_in_stock


class OrderLog(models.Model):

    class Meta:
        ordering = ["-created"]

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="logs", verbose_name=_("Order")
    )
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField(_("Message"))

    def __str__(self):
        return f"Log ID {self.pk} ({self.created})"
