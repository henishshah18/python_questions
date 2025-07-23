# mlmath.py

def dot_product(a, b):
    """
    Compute the dot product of two vectors.

    Args:
        a (list of numbers): First vector.
        b (list of numbers): Second vector.

    Returns:
        number: Dot product of a and b.

    Example:
        >>> dot_product([1, 2, 3], [4, 5, 6])
        32
    """
    return sum(x * y for x, y in zip(a, b))


def matrix_multiply(A, B):
    """
    Multiply two matrices.

    Args:
        A (list of list of numbers): First matrix.
        B (list of list of numbers): Second matrix.

    Returns:
        list of list of numbers: Resultant matrix after multiplication.

    Example:
        >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
    """
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = 0
            for k in range(len(B)):
                s += A[i][k] * B[k][j]
            row.append(s)
        result.append(row)
    return result


def conditional_probability(events):
    """
    Calculate conditional probability P(A|B) = P(A and B) / P(B).

    Args:
        events (dict): Dictionary with keys 'A_and_B' and 'B', values are probabilities or counts.

    Returns:
        float: Conditional probability P(A|B).

    Example:
        >>> conditional_probability({'A_and_B': 0.2, 'B': 0.5})
        0.4
    """
    if 'A_and_B' not in events or 'B' not in events or events['B'] == 0:
        raise ValueError("Invalid input: Provide 'A_and_B' and nonzero 'B'.")
    return events['A_and_B'] / events['B']


# Example usage
if __name__ == "__main__":
    print(dot_product([1, 2, 3], [4, 5, 6]))
    print(matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print(conditional_probability({'A_and_B': 120, 'B': 400}))
