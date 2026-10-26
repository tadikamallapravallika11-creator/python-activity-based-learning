

resources = {
    "Projector": 5,
    "Laptop": 10,
    "Microphone": 4,
    "Speaker": 3
}

activities = [
    ("Technical Workshop", 1, {
        "Projector": 2,
        "Laptop": 4,
        "Microphone": 1,
        "Speaker": 1
    }),
    ("Coding Competition", 2, {
        "Projector": 2,
        "Laptop": 6,
        "Microphone": 2,
        "Speaker": 1
    }),
    ("Cultural Event", 3, {
        "Projector": 2,
        "Laptop": 2,
        "Microphone": 3,
        "Speaker": 2
    })
]


activities.sort(key=lambda activity: activity[1])

allocations = {}
shortages = {}
remaining = resources.copy()

print("CAMPUS RESOURCE ALLOCATION")
print("-" * 50)

for activity, priority, requirements in activities:
    allocations[activity] = {}
    shortages[activity] = {}

    print(f"\nActivity: {activity} (Priority {priority})")

    for resource, required in requirements.items():
        available = remaining.get(resource, 0)
        allocated = min(required, available)
        shortage = required - allocated

        allocations[activity][resource] = allocated
        shortages[activity][resource] = shortage

        remaining[resource] -= allocated

        print(
            f"{resource}: Required={required}, "
            f"Allocated={allocated}, Shortage={shortage}"
        )

print("\n" + "-" * 50)
print("FINAL RESOURCE SUMMARY")

for resource in resources:
    print(
        f"{resource}: Initially Available={resources[resource]}, "
        f"Allocated={resources[resource] - remaining[resource]}, "
        f"Remaining={remaining[resource]}"
    )

print("\nSHORTAGE REPORT")

for activity, resource_data in shortages.items():
    missing = {
        resource: amount
        for resource, amount in resource_data.items()
        if amount > 0
    }

    if missing:
        print(activity, ":", missing)
    else:
        print(activity, ": No shortages")

print("\nFEASIBILITY CHECK")

for activity, priority, requirements in activities:
    feasible = all(
        allocations[activity][resource] == required
        for resource, required in requirements.items()
    )

    print(
        activity,
        "->",
        "Fully Feasible" if feasible else "Partially Feasible"
    )

