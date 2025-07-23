school = {
    "Math": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 92), ("Carol", 78)]
    },
    "Science": {
        "teacher": "Ms. Johnson",
        "students": [("David", 88), ("Eve", 94), ("Frank", 82)]
    }
}

print("Teacher Names:")
for class_name, class_info in school.items():
    print(f"- {class_name}: {class_info['teacher']}")

print("\nClass Average Grades:")
for class_name, class_info in school.items():
    total_grades = 0
    num_students = 0
    for student_name, grade in class_info['students']:
        total_grades += grade
        num_students += 1
    if num_students > 0:
        average_grade = total_grades / num_students
        print(f"- {class_name}: {average_grade}")
    else:
        print(f"- {class_name}: No students to calculate average.")

top_student_name = ""
top_student_grade = -1

print("\nTop Student Across All Classes:")
for class_name, class_info in school.items():
    for student_name, grade in class_info['students']:
        if grade > top_student_grade:
            top_student_grade = grade
            top_student_name = student_name

print(f"The top student is {top_student_name} with a grade of {top_student_grade}.")
