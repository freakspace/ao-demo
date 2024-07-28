from django.contrib import admin

from .models import StockLocation, StockRecord

admin.site.register(StockLocation)
admin.site.register(StockRecord)
