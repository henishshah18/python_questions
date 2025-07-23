# Original list of employees: (name, salary, department)
employees = [
    ("Alice", 50000, "Engineering"),
    ("Bob", 60000, "Marketing"),
    ("Carol", 55000, "Engineering"),
    ("David", 45000, "Sales")
]

print("Original List:")
print(employees)

# 1. Sort by Salary (Ascending)
by_salary_asc = sorted(employees, key=lambda x: x[1])
print("\nSorted by Salary (Ascending):")
print(by_salary_asc)

# 2. Sort by Salary (Descending)
by_salary_desc = sorted(employees, key=lambda x: x[1], reverse=True)
print("\nSorted by Salary (Descending):")
print(by_salary_desc)

# 3. Sort by Department, Then by Salary
by_dept_then_salary = sorted(employees, key=lambda x: (x[2], x[1]))
print("\nSorted by Department, Then by Salary:")
print(by_dept_then_salary)

# 4. Create a Reversed List Without Modifying Original
reversed_employees = list(reversed(employees))
print("\nReversed List (Without Modifying Original):")
print(reversed_employees)

# 5. Sort by Name Length
by_name_length = sorted(employees, key=lambda x: len(x[0]))
print("\nSorted by Name Length:")
print(by_name_length)

# 6. Use of .sort() (Modifies Original)
employees_copy = employees.copy()
employees_copy.sort(key=lambda x: x[1])  # Sort by salary
print("\nUsing .sort() to modify the list (Sorted by Salary Ascending):")
print(employees_copy)

# 7. Use of sorted() (Creates New List)
new_sorted_list = sorted(employees, key=lambda x: x[2])  # Sort by department
print("\nUsing sorted() to create a new list (Sorted by Department):")
print(new_sorted_list)
