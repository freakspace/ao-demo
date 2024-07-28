from django.views.generic import DetailView, ListView
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from orders.models import Order, OrderLog

from orders.utils import create_test_order


class OrderDetailView(DetailView):
    model = Order
    template_name = "orders/order_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_ready_for_pickup"] = self.object.is_ready_for_pickup()
        context["order_logs"] = OrderLog.objects.filter(order=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        line_id = request.POST.get("line_id")
        collected = request.POST.get("collected")
        # Mark the line as received
        if line_id:
            line = self.object.lines.get(pk=line_id)
            line.received = True

            OrderLog.objects.create(
                order=self.object, message=f"Orderline ID {line_id} has been received"
            )

            line.save()

            messages.success(request, _(f"Order line has been marked as collected"))

        # Mark the order as collected
        elif collected:
            self.object.order_status = "Collected"
            self.object.save()
            OrderLog.objects.create(
                order=self.object,
                message=f"Order ID { self.object.pk} has been collected by customer",
            )

            self.object.deduct_stock()

            messages.success(request, _(f"Order has been marked as collected"))
        else:
            messages.warning(request, _(f"No action was taken"))
        return redirect("orders:order_detail", pk=self.object.pk)


class OrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"

    def post(self, request, *args, **kwargs):
        order = create_test_order()

        if order:
            OrderLog.objects.create(order=order, message="Order has been created")

            messages.success(
                request, _(f"A test order id {order.pk} has been created.")
            )
        else:
            messages.warning(request, _(f"There was an error creating the order."))
        return redirect("orders:order_list")
