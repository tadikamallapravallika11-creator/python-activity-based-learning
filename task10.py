balance = 5000

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Amount")

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
        else:
            print("Invalid Amount or Insufficient Balance")

    elif choice == 3:
        print("Current Balance:", balance)

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid Choice")