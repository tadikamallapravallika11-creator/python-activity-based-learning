

transactions = [
    ("T101", 5000, "DEPOSIT"),
    ("T102", 2000, "WITHDRAWAL"),
    ("T103", -500, "DEPOSIT"),
    ("T104", 8000, "WITHDRAWAL"),
    ("T102", 1000, "DEPOSIT"),
    ("T105", 50000, "WITHDRAWAL"),
    ("T106", 3000, "DEPOSIT")
]

seen_ids = set()
duplicate_ids = []
invalid_transactions = []
suspicious_transactions = []

balance = 10000
total_deposits = 0
total_withdrawals = 0

print("TRANSACTION AUDIT")
print("-" * 50)

for transaction in transactions:
    transaction_id, amount, transaction_type = transaction


    if transaction_id in seen_ids:
        duplicate_ids.append(transaction_id)
        print("Duplicate Transaction ID:", transaction_id)
        continue

    seen_ids.add(transaction_id)


    if (
        not isinstance(amount, (int, float))
        or isinstance(amount, bool)
        or amount <= 0
        or transaction_type not in ("DEPOSIT", "WITHDRAWAL")
    ):
        invalid_transactions.append(transaction)
        print("Invalid Transaction:", transaction)
        continue


    if amount > 20000:
        suspicious_transactions.append(transaction)
        print("Suspicious Transaction:", transaction)


    if transaction_type == "DEPOSIT":
        balance += amount
        total_deposits += amount

    elif transaction_type == "WITHDRAWAL":
        if amount > balance:
            print("Insufficient Balance:", transaction_id)
            continue

        balance -= amount
        total_withdrawals += amount

    print(
        transaction_id,
        transaction_type,
        amount,
        "Balance:", balance
    )

print("\n" + "-" * 50)
print("AUDIT SUMMARY")
print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", balance)
print("Duplicate IDs:", duplicate_ids)
print("Invalid Transactions:", invalid_transactions)
print("Suspicious Transactions:", suspicious_transactions)
