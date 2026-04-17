def add_product(inventory, name, price, quantity):
    if price < 0:
        print("Error: Price must be positive.")
        return False
    if quantity < 0:
        print("Error: Quantity must be positive.")
        return False

    inventory.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })
    return True


def show_inventory(inventory):

    if not inventory:
        print("Empty inventory.")
        return

    print("\n--- INVENTORY ---")
    print(f"{'Product':<15}{'Price':<10}{'Quantity':<10}")
    print("-" * 35)

    for p in inventory:
        print(f"{p['name']:<15}{p['price']:<10}{p['quantity']:<10}")


def search_product(inventory, name):

    for p in inventory:
        if p["name"].lower() == name.lower():
            return p
    return None


def update_product(inventory, name, new_price=None, new_quantity=None):

    product = search_product(inventory, name)
    if product:
        if new_price is not None:
            if new_price < 0:
                print("Negative price not allowed")
                return False
            product["price"] = new_price

        if new_quantity is not None:
            if new_quantity < 0:
                print("Negative quantity not allowed")
                return False
            product["quantity"] = new_quantity

        return True

    return False


def delete_product(inventory, name):

    product = search_product(inventory, name)
    if product:
        inventory.remove(product)
        return True
    return False


def calculate_statistics(inventory):

    if not inventory:
        return None

    total_units = sum(p["quantity"] for p in inventory)
    total_value = sum(p["price"] * p["quantity"] for p in inventory)

    most_expensive_product = max(inventory, key=lambda p: p["price"])
    highest_stock_product = max(inventory, key=lambda p: p["quantity"])

    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive_product": (
            most_expensive_product["name"],
            most_expensive_product["price"]
        ),
        "highest_stock_product": (
            highest_stock_product["name"],
            highest_stock_product["quantity"]
        )
    }