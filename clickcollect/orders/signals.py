from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import OrderLine, OrderLog


@receiver(post_save, sender=OrderLine)
def check_order_lines_send_email(sender, instance, **kwargs):
    """Check if all order lines are received and send email to customer"""
    order = instance.order

    if all(line.received for line in order.lines.all()):

        if not OrderLog.objects.filter(order=order, message="Email sent").exists():
            # TODO Send email to customer
            print("Email sent to customer")
            # Log the email sending event
            order.log_action("Email sent")
            # Mark order as Ready for customer pickup
            order.order_status = "Ready"
            order.save()
