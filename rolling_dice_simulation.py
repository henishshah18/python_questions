import random

count_7 = 0
count_2 = 0
count_gt_10 = 0
trials = 10000

for i in range(trials):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    s = d1 + d2
    if s == 7:
        count_7 += 1
    if s == 2:
        count_2 += 1
    if s > 10:
        count_gt_10 += 1

print(f"P(Sum = 7): {count_7 / trials}")
print(f"P(Sum = 2): {count_2 / trials}")
print(f"P(Sum > 10): {count_gt_10 / trials}")
