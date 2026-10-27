m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("Total Marks:", total)
print("Percentage:", percentage)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")