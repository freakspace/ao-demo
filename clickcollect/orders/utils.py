from orders.models import Customer, Order, OrderLine, Product, StockLocation


def create_test_order() -> Order:
    """Create a order for testing purpose with 3 order lines"""
    customer = Customer.objects.first()
    location = StockLocation.objects.first()
    products = Product.objects.all()

    # Create a test order
    order = Order.objects.create(
        customer=customer, total_excl_tax=0, location=location, order_status="Pending"
    )

    # Keep a track of order total
    total = 0

    # Create order lines
    for n, product in enumerate(products, start=1):
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
