sales_data = [
    ("Q1", [("Jan", 1000), ("Feb", 1200), ("Mar", 1100)]),
    ("Q2", [("Apr", 1300), ("May", 1250), ("Jun", 1400)]),
    ("Q3", [("Jul", 1350), ("Aug", 1450), ("Sep", 1300)])
]

# 1. Total Sales per Quarter
print("Total Sales per Quarter:")
for quarter, months in sales_data:
    total = 0
    for month, sales in months:
        total += sales
    print(f"{quarter}: {total}")

# 2. Month with Highest Sales
highest_month = ("", 0)
for _, months in sales_data:
    for month, sales in months:
        if sales > highest_month[1]:
            highest_month = (month, sales)
print(f"\nMonth with Highest Sales: {highest_month[0]} ({highest_month[1]})")

# 3. Flat List of Monthly Sales
flat_list = []
for _, months in sales_data:
    for month_sales in months:
        flat_list.append(month_sales)
print("\nFlat List of Monthly Sales:")
print(flat_list)

# 4. Use Unpacking in Loops
print("\nDetailed Sales Report:")
for quarter, months in sales_data:
    print(f"{quarter}:")
    for month, sales in months:
        print(f"  {month}: {sales}")
