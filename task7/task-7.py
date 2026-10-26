

students = {
    "Team A": [
        ("S101", [80, 85, 90]),
        ("S102", [75, 80, 85]),
        ("S103", [90, 88, 92])
    ],
    "Team B": [
        ("S104", [85, 85, 90]),
        ("S105", [80, 85, 85]),
        ("S106", [80, 78, 82])
    ],
    "Team C": [
        ("S107", [90, 90, 90]),
        ("S108", [85, 85, 85])
    ]
}

MIN_SIZE = 3
MAX_SIZE = 5

team_results = []

print("HACKATHON TEAM ANALYSIS")
print("-" * 50)

for team, members in students.items():

    
    if not MIN_SIZE <= len(members) <= MAX_SIZE:
        print(f"{team}: Invalid team size ({len(members)} members)")
        continue

    total_score = 0
    round_totals = [0, 0, 0]
    valid_team = True

    
    for student_id, scores in members:
        if len(scores) != 3 or any(
            not isinstance(score, (int, float))
            or isinstance(score, bool)
            or not 0 <= score <= 100
            for score in scores
        ):
            print(f"Invalid scores for {student_id}")
            valid_team = False
            break

        total_score += sum(scores)

        for i, score in enumerate(scores):
            round_totals[i] += score

    if not valid_team:
        continue

    team_results.append({
        "team": team,
        "members": len(members),
        "rounds": round_totals,
        "total": total_score
    })

    print(f"\n{team}")
    print("Members:", len(members))
    print("Round 1 Total:", round_totals[0])
    print("Round 2 Total:", round_totals[1])
    print("Round 3 Total:", round_totals[2])
    print("Overall Score:", total_score)


