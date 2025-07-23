inventory = {
    "apples": {"price": 1.50, "quantity": 100},
    "bananas": {"price": 0.75, "quantity": 150},
    "oranges": {"price": 2.00, "quantity": 80}
}

inventory["grapes"] = {"price": 2.50, "quantity": 60}
inventory["bananas"]["price"] = 0.85
inventory["apples"]["quantity"] -= 25

total_value = sum(item["price"] * item["quantity"] for item in inventory.values())
print("Total Inventory Value:", total_value)

low_stock = [product for product, data in inventory.items() if data["quantity"] < 100]
print("Low Stock Products:", low_stock)
