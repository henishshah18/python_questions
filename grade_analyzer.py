grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

sliced = grades[2:8]
above_85 = [g for g in grades if g > 85]
grades[3] = 95
grades.extend([86, 93, 80])
grades.sort(reverse=True)
top_5 = grades[:5]

print("Sliced:", sliced)
print("Above 85:", above_85)
print("Top 5:", top_5)
