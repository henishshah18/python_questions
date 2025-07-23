import numpy as np

def add_vectors(a, b):
    return list(np.add(a, b))

def dot_product(a, b):
    return int(np.dot(a, b))

def are_orthogonal(a, b):
    return np.dot(a, b) == 0

a = [1, 2, 3]
b = [4, 5, 6]

print("Sum:", add_vectors(a, b))
print("Dot Product:", dot_product(a, b))
print("Orthogonal:", are_orthogonal(a, b))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)
print("Matrix Multiplication Result:")
print(result)
