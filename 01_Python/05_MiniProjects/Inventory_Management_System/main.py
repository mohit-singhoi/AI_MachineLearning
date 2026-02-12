# main.py

from inventory import InventorySystem
from product import Product


def main():
    inventory = InventorySystem()

    while True:
        print("\n====== Inventory Management System ======")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Quantity")
        print("4. Delete Product")
        print("5. Total Inventory Value")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            inventory.view_products()

        elif choice == "2":
            pid = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))

            product = Product(pid, name, quantity, price)
            inventory.add_product(product)
            print("Product added successfully!")

        elif choice == "3":
            pid = input("Enter Product ID to update: ")
            quantity = int(input("Enter new quantity: "))
            inventory.update_quantity(pid, quantity)

        elif choice == "4":
            pid = input("Enter Product ID to delete: ")
            inventory.delete_product(pid)

        elif choice == "5":
            inventory.total_inventory_value()

        elif choice == "6":
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
