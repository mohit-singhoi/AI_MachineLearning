# analyzer.py

import json
import os
from sale import Sale


class SalesAnalyzer:

    # Get absolute path of current file
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_PATH = os.path.join(BASE_DIR, "Data", "sales.json")

    def __init__(self):
        self.sales = []
        self.load_sales()

    def load_sales(self):
        try:
            with open(self.FILE_PATH, "r") as f:
                data = json.load(f)
                self.sales = [
                    Sale(d["product"], d["quantity"], d["price"])
                    for d in data
                ]
        except FileNotFoundError:
            print("sales.json file not found!")
            self.sales = []

    def save_sales(self):
        with open(self.FILE_PATH, "w") as f:
            json.dump([s.to_dict() for s in self.sales], f, indent=4)

    def add_sale(self, sale):
        self.sales.append(sale)
        self.save_sales()

    def view_sales(self):
        if not self.sales:
            print("No sales records found")
        else:
            for sale in self.sales:
                print(sale)

    def total_revenue(self):
        total = sum(s.total_price() for s in self.sales)
        print("Total Revenue:", total)

    def best_product(self):
        product_totals = {}

        for s in self.sales:
            product_totals[s.product] = (
                product_totals.get(s.product, 0)
                + s.total_price()
            )

        if product_totals:
            best = max(product_totals, key=product_totals.get)
            print("Best Selling Product:", best)
        else:
            print("No data available")
