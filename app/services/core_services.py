# app/services/core_services.py
from app.models.models import Order, CreditCardProcessor

class OrderService:
    orders = []

    @classmethod
    def place_order(cls, customer):
        if not customer.cart:
            raise Exception("Cart is empty.")
        order = Order(customer, customer.cart)
        processor = CreditCardProcessor()
        processor.pay(order.total)
        order.status = order.status.PAID
        cls.orders.append(order)
        customer.cart = []  # clear cart
        return order
