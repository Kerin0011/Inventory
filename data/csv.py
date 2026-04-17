import csv


def save_csv(inventory, path, include_header=True):
    """
    Saves the inventory to a CSV file.
    """
    if not inventory:
        print("No data to save.")
        return

    try:
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if include_header:
                writer.writerow(["name", "price", "quantity"])

            for p in inventory:
                writer.writerow([p["name"], p["price"], p["quantity"]])

        print(f"Inventory saved to: {path}")

    except Exception as e:
        print(f"Error saving file: {e}")


def load_csv(path):
    """
    Loads products from a CSV file.
    Returns a list of products.
    """
    inventory = []
    errors = 0

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)

            header = next(reader)
            if header != ["name", "price", "quantity"]:
                print("Invalid header.")
                return []

            for row in reader:
                if len(row) != 3:
                    errors += 1
                    continue

                try:
                    name = row[0]
                    price = float(row[1])
                    quantity = int(row[2])

                    if price < 0 or quantity < 0:
                        raise ValueError

                    inventory.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    })

                except:
                    errors += 1

        print(f"File loaded. Invalid rows: {errors}")
        return inventory

    except FileNotFoundError:
        print("File not found.")
    except UnicodeDecodeError:
        print("Encoding error.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return []