import json
import os
from datetime import datetime

GRADE_FILE = "grades.json"
SUBJECTS = ["Math", "Science", "English", "Computer", "Social"]

# Grade logic
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

# Save to grades.json
def save_record(data):
    records = []
    if os.path.exists(GRADE_FILE):
        with open(GRADE_FILE, 'r') as file:
            try:
                records = json.load(file)
            except json.JSONDecodeError:
                records = []

    records.append(data)

    with open(GRADE_FILE, 'w') as file:
        json.dump(records, file, indent=4)

# Collect marks
def input_marks():
    marks = {}
    for subject in SUBJECTS:
        while True:
            try:
                score = int(input(f"Enter marks for {subject} (0–100): "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                else:
                    print("❌ Enter valid marks between 0–100.")
            except ValueError:
                print("❌ Please enter numeric value.")
    return marks

# Grade evaluation
def evaluate_student():
    print("\n🎓 Student Grade Entry")
    name = input("👤 Enter student name: ")

    marks = input_marks()
    total = sum(marks.values())
    average = total / len(SUBJECTS)
    overall_grade = get_grade(average)

    subject_grades = {subj: get_grade(score) for subj, score in marks.items()}

    student_record = {
        "Student Name": name,
        "Marks": marks,
        "Grades": subject_grades,
        "Total": total,
        "Average": round(average, 2),
        "Final Grade": overall_grade,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("\n📋 Grade Summary")
    for subject, score in marks.items():
        print(f"{subject}: {score} → Grade: {subject_grades[subject]}")
    print(f"\nTotal: {total}")
    print(f"Average: {average:.2f}")
    print(f"Overall Grade: {overall_grade}")

    save_record(student_record)
    print("✅ Student record saved.\n")

# Main loop
def main():
    while True:
        evaluate_student()
        again = input("➕ Enter another student? (y/n): ").lower()
        if again != 'y':
            print("📁 All records saved in 'grades.json'. Exiting.")
            break

main()
