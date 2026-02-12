# inventory.py

import json
import os
from product import Product


class InventorySystem:
    FILE_PATH = os.path.join("Data", "inventory.json")

    def __init__(self):
        self.products = []
        self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.FILE_PATH, "r") as f:
                data = json.load(f)
                self.products = [
                    Product(p["product_id"], p["name"], p["quantity"], p["price"])
                    for p in data
                ]
        except FileNotFoundError:
            self.products = []

    def save_inventory(self):
        with open(self.FILE_PATH, "w") as f:
            json.dump([p.to_dict() for p in self.products], f, indent=4)

    def add_product(self, product):
        self.products.append(product)
        self.save_inventory()

    def view_products(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            for p in self.products:
                print(p)

    def update_quantity(self, product_id, new_quantity):
        for p in self.products:
            if p.product_id == product_id:
                p.quantity = new_quantity
                self.save_inventory()
                print("Quantity updated successfully.")
                return
        print("Product not found.")

    def delete_product(self, product_id):
        for p in self.products:
            if p.product_id == product_id:
                self.products.remove(p)
                self.save_inventory()
                print("Product deleted successfully.")
                return
        print("Product not found.")

    def total_inventory_value(self):
        total = sum(p.total_value() for p in self.products)
        print("Total Inventory Value:", total)
