# Custom map function
def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

# Custom filter function
def my_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

# Custom reduce function
def my_reduce(func, iterable):
    result = iterable[0]
    for item in iterable[1:]:
        result = func(result, item)
    return result

numbers = [1, 2, 3, 4, 5, 6]

# 1️. Transform: Square each number (using custom map)
squares = my_map(lambda x: x ** 2, numbers)
print("Squares:", squares)

# 2️. Filter: Keep only even numbers (using custom filter)
evens = my_filter(lambda x: x % 2 == 0, numbers)
print("Even numbers:", evens) 

# 3️. Reduce: Compute product of all numbers (using custom reduce)
product = my_reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)
