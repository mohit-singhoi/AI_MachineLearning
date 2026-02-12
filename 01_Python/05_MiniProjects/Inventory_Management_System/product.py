# product.py

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.quantity * self.price

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

    def __str__(self):
        return (f"ID: {self.product_id} | "
                f"Name: {self.name} | "
                f"Qty: {self.quantity} | "
                f"Price: {self.price} | "
                f"Total Value: {self.total_value()}")
