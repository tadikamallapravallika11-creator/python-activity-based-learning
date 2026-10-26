

classrooms = {
    "Classroom A": [
        [None, None, "RESERVED"],
        [None, None, None]
    ],
    "Classroom B": [
        [None, "RESERVED", None],
        [None, None, None]
    ]
}

assignments = {
    "Classroom A": [
        (1, 1, "Student101"),
        (1, 2, "Student102"),
        (2, 1, "Student103")
    ],
    "Classroom B": [
        (1, 1, "Student104"),
        (1, 3, "Student105"),
        (2, 1, "Student101")
    ]
}

assigned_students = set()
total_seats = 0
occupied_seats = 0
reserved_seats = 0
duplicates = []

for room, seating in classrooms.items():
    print("\n", room)

    for row, col, student in assignments[room]:
        r, c = row - 1, col - 1

        if not (0 <= r < len(seating) and
                0 <= c < len(seating[r])):
            print("Invalid seat:", student)
            continue

        if student in assigned_students:
            duplicates.append(student)
            print("Duplicate assignment detected:", student)
            continue

        if seating[r][c] == "RESERVED":
            print("Seat is reserved for:", student)
            continue

        if seating[r][c] is not None:
            print("Seat already occupied:", student)
            continue

        seating[r][c] = student
        assigned_students.add(student)

    for row in seating:
        print(row)

    for row in seating:
        total_seats += len(row)
        for seat in row:
            if seat == "RESERVED":
                reserved_seats += 1
            elif seat is not None:
                occupied_seats += 1

vacant_seats = total_seats - occupied_seats - reserved_seats

print("\n--- Occupancy Summary ---")
print("Total Seats:", total_seats)
print("Occupied Seats:", occupied_seats)
print("Reserved Seats:", reserved_seats)
print("Vacant Seats:", vacant_seats)
print("Unique Students:", len(assigned_students))
print("Duplicate Assignments:", duplicates)
