# sale.py

class Sale:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price

    def to_dict(self):
        return {
            "product": self.product,
            "quantity": self.quantity,
            "price": self.price
        }

    def __str__(self):
        return f"{self.product} | Qty: {self.quantity} | Price: {self.price} | Total: {self.total_price()}"
