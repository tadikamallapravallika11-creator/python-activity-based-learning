

products = [
    ("P101", 500.0, 10),
    ("P102", 250.0, 3),
    ("P103", 1200.0, 0),
    ("P104", -100.0, 5),
    ("P105", 300.0, -2),
    ("P106", 150.0, 4)
]

reorder_level = 5
total_inventory_value = 0
invalid_records = []
replenishment_items = []

print("PRODUCT CATALOGUE AUDIT")
print("-" * 50)

for product in products:
    product_id, price, stock = product

    # Detect invalid records
    if not product_id or price < 0 or stock < 0:
        invalid_records.append(product)
        print("Invalid Record:", product)
        continue

    # Calculate inventory value
    inventory_value = price * stock
    total_inventory_value += inventory_value

    print("Product ID:", product_id)
    print("Price:", price)
    print("Stock:", stock)
    print("Inventory Value:", inventory_value)

    # Identify items requiring replenishment
    if stock <= reorder_level:
        replenishment_items.append(product_id)

print("\n" + "-" * 50)
print("AUDIT SUMMARY")
print("Total Valid Inventory Value:", total_inventory_value)
print("Invalid Records:", invalid_records)
print("Items Requiring Replenishment:", replenishment_items)
print("Total Valid Products:", len(products) - len(invalid_records))
