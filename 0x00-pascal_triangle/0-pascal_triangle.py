#!/use/bin/python3
""" Pascal triangle function modeule """


def pascal_triangle(n):
    """ finds and retuens the pascal triangle for a given range of number n """
    if n <= 0:
        return []
    triangle = [0] * n
    for i in range(n):
        row = [0] * (i + 1)
        row[0], row[-1] = 1, 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle[i] = row
    return triangle
