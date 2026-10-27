products = ["Pen", "Book", "Pencil"]

opening = [100, 50, 80]
received = [20, 30, 10]
dispatched = [40, 15, 25]

for i in range(len(products)):
    closing = opening[i] + received[i] - dispatched[i]

    print("Product:", products[i])
    print("Closing Stock:", closing)
    print()