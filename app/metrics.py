from django.utils.formats import number_format
from product.models import Product


def get_product_metric():
    products=Product.objects.all()
    total_cost_price = sum(product.cost_price * product.quantity for product in products)
    total_seling_price = sum(product.selling_price * product.quantity for product in products)
    total_quantity = sum(product.quantity for product in products)
    total_profit = total_seling_price - total_cost_price

    return dict(
        total_cost_price=number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        total_seling_price=number_format(total_seling_price, decimal_pos=2, force_grouping=True),
        total_quantity=total_quantity,
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
    )

    