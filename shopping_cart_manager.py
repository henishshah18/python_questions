# Shopping Cart Manager

cart = []

cart.append("apples")
cart.append("bread")
cart.append("milk")
cart.append("eggs")

item_to_remove = "bread"
if item_to_remove in cart:
    cart.remove(item_to_remove)
if cart:
    cart.pop()
sorted_cart = sorted(cart)
print("Cart in Alphabetical Order:")
for item in sorted_cart:
    print(item)

print("\nFinal Cart with Indices:")

for index, item in enumerate(cart):
    print(f"{index}: {item}")
