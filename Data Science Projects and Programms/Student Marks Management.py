#Student Marks Management
#
#👉 Create a Python program to:
#	•	Store student names as keys and marks as values in a dictionary.
#	•	Allow adding new students with marks.
#	•	Allow updating marks of existing students.
#	•	Display highest, lowest, and average marks.
#	•	Show all records.

student_marks = {}
def add_student():
    name = input("Enter student name: ")
    if name in student_marks:
        print("Student already exists.")
    else:
            marks = float(input("Enter marks: "))
            student_marks[name] = marks
            print(f"{name} added successfully.")
def update_marks():
    name = input("Enter student name to update: ")
    if name in student_marks:
            marks = float(input("Enter new marks: "))
            student_marks[name] = marks
            print(f"{name}'s marks updated successfully.")
    else:
        print("Student not found.")
def display_statistics():
    if not student_marks:
        print("No records to show.")
        return
    marks_list = list(student_marks.values())
    highest = max(marks_list)
    lowest = min(marks_list)
    average = sum(marks_list) / len(marks_list)

    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Average Marks: {average:.2f}")
def show_all():
    if not student_marks:
        print("No student records available.")
    else:
        print("\nAll Student Records:")
        for name, marks in student_marks.items():
            print(f"{name}: {marks}")
while True:
    print("\n--- Student Marks Management ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display Statistics")
    print("4. Show All Records")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_student()
    elif choice == '2':
        update_marks()
    elif choice == '3':
        display_statistics()
    elif choice == '4':
        show_all()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
