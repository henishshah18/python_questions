import math

# 1️. Factorial approximation
factorial = lambda n: round(math.gamma(n + 1))
print("Factorial Approximation of 5:", factorial(5))

# 2️. Convert string to uppercase
to_upper = lambda s: s.upper()
print("Uppercase of 'lambda':", to_upper("lambda"))

# 3️. Sum of elements in a list
sum_list = lambda lst: sum(lst)
print("Sum of [1, 2, 3, 4]:", sum_list([1, 2, 3, 4]))
