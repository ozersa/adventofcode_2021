"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?

"""

#import sys
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