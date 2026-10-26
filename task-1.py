

subjects = int(input("Enter number of subjects: "))
max_marks = 100
pass_marks = 35
grace_limit = 5

total = 0
results = []
failed_subjects = []

for i in range(subjects):
    name = input(f"\nEnter subject {i + 1} name: ")
    marks = int(input(f"Enter marks in {name} (out of 100): "))

    if marks < 0 or marks > max_marks:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue

    grace = 0

    if marks < pass_marks and marks + grace_limit >= pass_marks:
        grace = pass_marks - marks
        marks += grace

    marks = min(marks, max_marks)
    total += marks

    if marks >= pass_marks:
        status = "PASS"
    else:
        status = "FAIL"
        failed_subjects.append(name)

    results.append((name, marks, grace, status))

print("\n========== EXAMINATION RESULT ==========")

for name, marks, grace, status in results:
    print(f"Subject: {name}")
    print(f"Final Marks: {marks}/100")
    print(f"Grace Marks: {grace}")
    print(f"Status: {status}")
    print("----------------------------------------")

print("Total Marks:", total, "/", len(results) * max_marks)

if failed_subjects:
    print("Overall Result: FAIL")
    print("Failed Subjects:", ", ".join(failed_subjects))
else:
    print("Overall Result: PASS")

if results:
    percentage = total / (len(results) * max_marks) * 100
    print(f"Percentage: {percentage:.2f}%")

    if not failed_subjects:
        if percentage >= 75:
            classification = "Distinction"
        elif percentage >= 60:
            classification = "First Class"
        elif percentage >= 50:
            classification = "Second Class"
        else:
            classification = "Pass Class"

        print("Classification:", classification)
    else:
        print("Classification: Not Classified")
