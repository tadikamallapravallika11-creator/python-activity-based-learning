

attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes conducted: "))
threshold = float(input("Enter eligibility percentage: "))

if total < 0 or attended < 0 or attended > total:
    print("Invalid attendance details!")

elif not 0 < threshold <= 100:
    print("Invalid eligibility percentage!")

else:
    if total == 0:
        print("No classes conducted yet.")
        current = 0
    else:
        current = (attended / total) * 100

    print(f"\nCurrent Attendance: {current:.2f}%")

    if current >= threshold:
        print("Status: Eligible")
        print("Additional classes required: 0")

    else:
        required = 0

        while ((attended + required) /
               (total + required)) * 100 < threshold:
            required += 1

        print("Status: Not Eligible")
        print("Minimum consecutive classes required:", required)

    # Future attendance scenarios
    print("\nFuture Attendance Scenarios")

    for future in [5, 10, 20]:
        percentage = (
            (attended + future) / (total + future)
        ) * 100

        print(
            f"After attending {future} classes: "
            f"{percentage:.2f}%"
        )

        if percentage >= threshold:
            print("  Eligibility: Eligible")
        else:
            print("  Eligibility: Not Eligible")

