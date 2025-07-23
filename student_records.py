students = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 19),
    (103, "Carol", 78, 21),
    (104, "David", 88, 20)
]

# 1. Find the Student with the Highest Grade
highest_grade_student = max(students, key=lambda x: x[2])
print("Student with the highest grade:", highest_grade_student)

# 2. Create a Name-Grade List
name_grade_list = [(student[1], student[2]) for student in students]
print("Name-Grade List:", name_grade_list)

# 3. Demonstrate Tuple Immutability
try:
    students[0][2] = 90  # Attempting to modify the grade
except TypeError as e:
    print("Error:", e)

# Why tuples?
print("\nTuples are immutable, which means student records cannot be accidentally changed.\n"
      "They are ideal for storing fixed-format, read-only data such as database-like rows.")
