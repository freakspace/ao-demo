from django.db import models

from django.utils.translation import gettext as _


class Customer(models.Model):
    name = models.CharField(
        _("Customer name"),
        help_text=_("name of the order"),
        max_length=255,
    )
    email = models.EmailField(
        _("Email"), help_text=_("Email of the customers"), max_length=255
    )

    def __str__(self):
        return self.name
