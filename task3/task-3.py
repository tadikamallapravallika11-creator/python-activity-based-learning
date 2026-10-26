

balance = float(input("Enter initial balance: "))
withdrawal_limit = 10000

transactions = []
total_deposits = 0
total_withdrawals = 0
rejected = 0

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = input("Enter transaction type (1/2): ")
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount!")
        rejected += 1
        transactions.append(("Invalid", amount, "Rejected"))
        continue

    if choice == "1":
        balance += amount
        total_deposits += amount
        transactions.append(("Deposit", amount, "Successful"))
        print("Deposit successful!")

    elif choice == "2":
        if amount > withdrawal_limit:
            print("Withdrawal limit exceeded!")
            rejected += 1
            transactions.append(("Withdrawal", amount, "Rejected"))

        elif amount > balance:
            print("Insufficient balance!")
            rejected += 1
            transactions.append(("Withdrawal", amount, "Rejected"))

        else:
            balance -= amount
            total_withdrawals += amount
            transactions.append(("Withdrawal", amount, "Successful"))
            print("Withdrawal successful!")

    else:
        print("Invalid transaction type!")
        rejected += 1
        transactions.append(("Invalid", amount, "Rejected"))

print("\n===== ATM TRANSACTION SUMMARY =====")

for i, (t_type, amount, status) in enumerate(transactions, 1):
    print(
        f"{i}. {t_type} | Amount: Rs.{amount:.2f} "
        f"| Status: {status}"
    )

print("-----------------------------------")
print(f"Total Deposits: Rs.{total_deposits:.2f}")
print(f"Total Withdrawals: Rs.{total_withdrawals:.2f}")
print(f"Rejected Transactions: {rejected}")
print(f"Final Balance: Rs.{balance:.2f}")

