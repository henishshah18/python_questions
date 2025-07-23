# Input data
students = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
scores = [85, 92, 78, 95, 88]

# 1. Numbered List of Students
print("1. Numbered List of Students:")
for i, name in enumerate(students, start=1):
    print(f"{i}. {name}")
print()

# 2. Pair Students with Their Scores
print("2. Students with Scores:")
for name, score in zip(students, scores):
    print(f"{name}: {score}")
print()

# 3. Positions of High Scorers (>90)
print("3. Positions of High Scorers (score > 90):")
high_scorer_indices = [i for i, score in enumerate(scores) if score > 90]
print(high_scorer_indices)
print()

# 4. Map Positions to Student Names
print("4. Dictionary of Position to Student Name:")
position_to_name = {i: name for i, name in enumerate(students)}
print(position_to_name)
