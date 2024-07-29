from django.contrib import admin

from .models import Order, OrderLine, OrderLog


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    max_num = 1


class OrderLogInline(admin.TabularInline):
    model = OrderLog
    max_num = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline, OrderLogInline]
    list_display = (
        "customer",
        "created",
        "total_excl_tax",
        "location",
        "order_status",
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
