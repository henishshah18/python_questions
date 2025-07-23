products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [999.99, 25.50, 75.00, 299.99]
quantities = [5, 20, 15, 8]


product_price_pairs = list(zip(products, prices))
total_values = [price * qty for price, qty in zip(prices, quantities)]
catalog = {
    product: {"price": price, "quantity": qty}
    for product, price, qty in zip(products, prices, quantities)
}
low_stock = [product for product, qty in zip(products, quantities) if qty < 10]

print("Product-Price Pairs:", product_price_pairs)
print("Total Inventory Values:", total_values)
print("Product Catalog:", catalog)
print("Low Stock Products:", low_stock)
