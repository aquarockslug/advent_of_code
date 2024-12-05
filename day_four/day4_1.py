import re

# Day four #1 by Aquarocks


data = []
with open("data.txt") as f:
    for line in f.readlines():
        data.append(list(line.strip()))

TARGET = "XMAS"


def search_lines(data, count=0):
    for line in data:
        count += len(re.findall(TARGET, str(line)))
        count += len(re.findall(TARGET, str(reversed(line))))
    return count


def rotatedOrder(data):
    transposed_image = [
        [data[j][i] for j in range(len(data))] for i in range(len(data[0]))
    ]
    return transposed_image
    # return [list(reversed(row)) for row in transposed_image]


def diagonal_lines(matrix, d=[]):
    ROW = len(matrix)
    COL = len(matrix[0])
    for line in range(1, (ROW + COL)):
        start_col = max(0, line - ROW)
        count = min(line, (COL - start_col), ROW)
        chars = []
        for j in range(0, count):
            chars.append(matrix[min(ROW, line) - j - 1][start_col + j])
        d.append("".join(chars))
    return d


def rotated_lines(matrix, d=[]):
    rotated = rotatedOrder(matrix)
    for i in range(0, len(rotated)):
        d.append("".join(rotated[i]))
    return d


def lines(matrix, d=[]):
    for row in matrix:
        d.append("".join(row))
    return d


directions = [
    search_lines(lines(data)),
    search_lines(rotated_lines(data)),
    search_lines(diagonal_lines(data)),
    search_lines(diagonal_lines(rotatedOrder(data))),
]
print(f"{directions}\n = {sum(directions)}")
