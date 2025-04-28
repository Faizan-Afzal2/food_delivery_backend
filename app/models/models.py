# app/models.py
import uuid
from abc import ABC, abstractmethod
from enum import Enum

class OrderStatus(Enum):
    PENDING = "Pending"
    PAID = "Paid"
    DELIVERED = "Delivered"

class Customer:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

class Restaurant:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.menu = []

    def add_menu_item(self, item):
        self.menu.append(item)

class MenuItem:
    def __init__(self, name, price):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price

class Order:
    def __init__(self, customer, items):
        self.id = str(uuid.uuid4())
        self.customer = customer
        self.items = items
        self.total = sum(item.price for item in items)
        self.status = OrderStatus.PENDING

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount): pass

class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} via credit card.")
