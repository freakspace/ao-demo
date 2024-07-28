from orders.models import Customer, Order, OrderLine, Product, StockLocation


def create_test_order() -> Order:
    customer = Customer.objects.first()
    location = StockLocation.objects.first()
    product = Product.objects.first()

    # Create a test order
    order = Order.objects.create(
        customer=customer, total_excl_tax=0, location=location, order_status="Pending"
    )

    # Keep a track of order total
    total = 0

    # Create x order lines
    for n in range(1, 4):

        # Use n as quantity just for testing
        line = OrderLine.objects.create(
            order=order,
            product=product,
            quantity=n,
            title=product.name,
            unit_price=product.unit_price,
        )

        total += line.quantity * line.unit_price

    order.total_excl_tax = total
    order.save()

    return order
