# 1. Simple List Creation:

# Traditional
squares = []
for i in range(1, 6):
    squares.append(i * i)

squares = [i * i for i in range(1, 6)]
print("Squares:", squares)


# 2. Filtering Condition

# Traditional
evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)

evens = [i for i in range(10) if i % 2 == 0]
print("Evens:", evens)


# 3. Nested Loops: Cartesian product of two lists

# Traditional
pairs = []
for x in [1, 2]:
    for y in [3, 4]:
        pairs.append((x, y))

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print("Pairs:", pairs)
