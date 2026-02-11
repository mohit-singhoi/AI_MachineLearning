# main.py

from analyzer import SalesAnalyzer
from sale import Sale


def main():
    analyzer = SalesAnalyzer()

    while True:
        print("\n===== Sales Data Analyzer =====")
        print("1. Add Sale")
        print("2. View Sales")
        print("3. Total Revenue")
        print("4. Best Selling Product")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            product = input("Product Name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            sale = Sale(product, quantity, price)
            analyzer.add_sale(sale)
            print("Sale added successfully!")

        elif choice == "2":
            analyzer.view_sales()

        elif choice == "3":
            analyzer.total_revenue()

        elif choice == "4":
            analyzer.best_product()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
