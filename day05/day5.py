import sys
#from day5_1_input import *
from day5_2_input import *


cordinates = list()

xmax = 0
ymax = 0

for line in str_input.split('\n'):
    if line == "":
        continue

    x1y1, x2y2 = list(line.split('->'))

    x1, y1 = x1y1.strip().split(',')
    x2, y2 = x2y2.strip().split(',')

    x1, y1 = int(x1), int(y1)
    x2, y2 = int(x2), int(y2)

    xmax = max(x1, x2, xmax)
    ymax = max(y1, y2, ymax)

    cordinates.append([x1, y1, x2, y2])

#print(xmax, ymax)

points = [[0 for i in range(xmax+1)] for j in range(ymax+1)]


def print_points():
    print("---------------")
    for l in points:
        print(l)


#for x1, y1, x2, y2 in cordinates:
#    if (x1 == x2) or (y1 == y2):
#        print(x1, y1, " ", x2, y2)
#    elif abs(x2-x1) == abs(y2-y1):
#        print(x1, y1, " ", x2, y2)

print("-------------------------------------")

for x1, y1, x2, y2 in cordinates:
    if x1 == x2:
        start = min(y1, y2)
        end = max(y1, y2)
        #print("x1=x2", start, end)
        for i in range(start, end+1):
            points[i][x1] += 1

    elif y1 == y2:
        start = min(x1, x2)
        end = max(x1, x2)
        #print("y1=y2", start, end)
        for i in range(start, end+1):
            points[y1][i] += 1

    elif abs(x2-x1) == abs(y2-y1):
        x_plus = 1 if x2 > x1 else -1
        y_plus = 1 if y2 > y1 else -1

        for i in range(abs(x2-x1)+1):
            points[y1+y_plus*i][x1+x_plus*i] += 1

#print_points()

count0 = 0
count1 = 0
total_count2_and_more = 0

for line in points:
    total_count2_and_more += len(line)

    total_count2_and_more -= line.count(0)
    total_count2_and_more -= line.count(1)

print("Total Count: ", total_count2_and_more)