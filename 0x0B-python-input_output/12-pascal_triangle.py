#!/usr/bin/python
"""Function Module."""


def pascal_triangle(n):
    """A function that print triangle of lists.

    Args:
        n: The size of triangle.

    Returns a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
