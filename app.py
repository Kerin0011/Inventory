from functions.services import *
from data.csv import *

inventory = []

while True:
    print("\n--- MENU ---")
    print("1. Add")
    print("2. Show")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Statistics")
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")

    option = input("Select an option: ")

    try:
        if option == "1":
            name = input("Name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            if add_product(inventory, name, price, quantity):
                print("Product added successfully.")
            else:
                print("Could not add the product.")

        elif option == "2":
            show_inventory(inventory)

        elif option == "3":
            name = input("Product to search: ")
            p = search_product(inventory, name)
            print(p if p else "Not found")

        elif option == "4":
            name = input("Product to update: ")

            price_input = input("New price (press enter to skip): ")
            quantity_input = input("New quantity (press enter to skip): ")

            price = float(price_input) if price_input != "" else None
            quantity = int(quantity_input) if quantity_input != "" else None

            result = update_product(inventory, name, price, quantity)

            if result:
                print("Product updated successfully.")
            else:
                print("Could not update the product.")

        elif option == "5":
            name = input("Product to delete: ")
            if delete_product(inventory, name):
                print("Product deleted.")
            else:
                print("Not found.")

        elif option == "6":
            stats = calculate_statistics(inventory)
            print(stats if stats else "Empty inventory")

        elif option == "7":
            path = input("File path: ")
            save_csv(inventory, path)

        elif option == "8":
            path = input("File path: ")
            new_items = load_csv(path)

            if new_items:
                decision = input("Overwrite inventory? (Y/N): ").lower()

                if decision == "y":
                    inventory = new_items
                else:
                    for new in new_items:
                        existing = search_product(inventory, new["name"])
                        if existing:
                            existing["quantity"] += new["quantity"]
                            existing["price"] = new["price"]
                        else:
                            inventory.append(new)

        elif option == "9":
            print("Exiting...")
            break

        else:
            print("Invalid option")

    except ValueError:
        print("Invalid input, try again.")
