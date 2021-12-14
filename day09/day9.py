import sys
from day9_1_input import *
from day9_2_input import *

numbers = list()
for line in str_input.split('\n'):
    if line == "":
        continue
    numbers.append(['9'] + list(line) + ['9'])

cols = len(numbers[0])
numbers.insert(0, ['9'] * cols)
numbers.append(['9'] * cols)
rows = len(numbers)

#print(rows, cols)

min_points = list()

def process_question1():
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            h = numbers[r][c]
            if h < numbers[r + 1][c]:
                if h < numbers[r - 1][c]:
                    if h < numbers[r][c + 1]:
                        if h < numbers[r][c - 1]:
                            min_points.append((r, c, h))

    total = 0
    for l in min_points:
        r, c, h = l
        total += int(h) + 1
        #print(l)

    print("Q1 Risk Level: ", total)


def process_question2():
    basins = list()
    points = list()

    def go_next(r, c):
        if (r, c) not in points:
            points.append((r, c))

        if (numbers[r][c] < numbers[r+1][c]) and (numbers[r+1][c] != '9'):
            go_next(r+1, c)
        if (numbers[r][c] < numbers[r-1][c]) and (numbers[r-1][c] != '9'):
            go_next(r-1, c)
        if (numbers[r][c] < numbers[r][c+1]) and (numbers[r][c+1] != '9'):
            go_next(r, c+1)
        if (numbers[r][c] < numbers[r][c-1]) and (numbers[r][c-1] != '9'):
            go_next(r, c-1)

    for l in min_points:
        r, c, h = l
        points.clear()
        go_next(r, c)
        basins.append(len(points))

    basins.sort()
    print("Q2 Answer: ", basins[-1] * basins[-2] * basins[-3])

process_question1()
process_question2()

