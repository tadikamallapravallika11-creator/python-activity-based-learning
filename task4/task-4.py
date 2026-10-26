

n = int(input("Enter number of products: "))

products = []

for i in range(n):
    print(f"\nProduct {i + 1}")

    name = input("Enter product name: ")
    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    closing = int(input("Enter actual closing stock: "))
    minimum = int(input("Enter minimum required stock: "))

    if min(opening, incoming, dispatched, closing, minimum) < 0:
        print("Invalid quantities! Enter non-negative values.")
        continue

    if dispatched > opening + incoming:
        print("Warning: Dispatched quantity exceeds available stock.")

    expected = opening + incoming - dispatched
    discrepancy = closing - expected
    replenishment = max(0, minimum - closing)

    if discrepancy == 0:
        status = "Matched"
    elif discrepancy > 0:
        status = "Excess Stock"
    else:
        status = "Stock Shortage"

    products.append({
        "name": name,
        "opening": opening,
        "incoming": incoming,
        "dispatched": dispatched,
        "closing": closing,
        "expected": expected,
        "discrepancy": discrepancy,
        "replenishment": replenishment,
        "status": status
    })

print("\n========== INVENTORY REPORT ==========")

for p in products:
    print(f"\nProduct: {p['name']}")
    print(f"Opening Stock: {p['opening']}")
    print(f"Incoming Stock: {p['incoming']}")
    print(f"Dispatched Stock: {p['dispatched']}")
    print(f"Expected Closing Stock: {p['expected']}")
    print(f"Actual Closing Stock: {p['closing']}")
    print(f"Discrepancy: {p['discrepancy']}")
    print(f"Status: {p['status']}")
    print(f"Replenishment Required: {p['replenishment']}")

print("\n========== SUMMARY ==========")
print("Total Products Processed:", len(products))
print("Products with Discrepancies:",
      sum(p["discrepancy"] != 0 for p in products))
print("Total Replenishment Required:",
      sum(p["replenishment"] for p in products))

