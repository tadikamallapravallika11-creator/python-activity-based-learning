balance = 5000

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print("Deposit Successful")

elif choice == 2:
    amount = int(input("Enter withdrawal amount: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance or Invalid Amount")

elif choice == 3:
    print("Balance:", balance)

else:
    print("Invalid Choice")

print("Final Balance:", balance)