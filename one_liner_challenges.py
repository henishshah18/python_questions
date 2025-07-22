from functools import reduce

#1️. Cube of odd numbers from 1 to 15 (list comprehension + condition)
odd_cubes = [i**3 for i in range(1, 16) if i % 2 != 0]
print('Odd cubes:', odd_cubes)

# 2️. Convert all strings in a list to uppercase (map + str.upper)
upper_words = list(map(str.upper, ['data', 'science', 'rocks']))
print('Upper words:', upper_words)

# 3️. Product of all numbers in a list using reduce (reduce + lambda)
product = reduce(lambda x, y: x * y, [2, 3, 4, 5])
print('Product:', product)

# 4️. Filter names starting with 'A' from a list (filter + lambda)
a_names = list(filter(lambda name: name.startswith('A'), ['Alice', 'Bob', 'Andrew', 'Eve']))
print('Names starting with A:', a_names)

# 5️. Square root of numbers using map and lambda (map + lambda)
import math
square_roots = list(map(lambda x: round(math.sqrt(x), 2), [4, 9, 16, 25, 36]))
print('Square roots:', square_roots)
