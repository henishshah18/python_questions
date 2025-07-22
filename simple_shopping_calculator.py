# Constants
TAX_RATE = 0.085  # 8.5%

# Input for 3 items
subtotal = 0
items = []

for i in range(1, 4):
    price = float(input(f"Enter price of item {i}: "))
    quantity = int(input(f"Enter quantity of item {i}: "))
    total = price * quantity
    items.append((price, quantity, total))
    subtotal += total

# Output each item's calculation
for i, (price, quantity, total) in enumerate(items, 1):
    print(f"Item {i}: {int(price)} x {quantity} = {int(total)}")

# Calculate and display tax and total
tax = subtotal * TAX_RATE
grand_total = subtotal + tax

print(f"Subtotal: {int(subtotal)}")
print(f"Tax (8.5%): {tax:.2f}")
print(f"Total: {grand_total:.2f}")
