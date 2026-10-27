rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

seat = 1

for i in range(rows):
    for j in range(cols):
        print("S" + str(seat), end="\t")
        seat += 1
    print()