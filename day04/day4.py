"""
--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

 After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

 Finally, 24 is drawn:

 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

 At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

"""

import sys
#from day4_1_input import *
from day4_2_input import *

numbers = list(str_numbers.split(','))

boards = list()
b = list()
for line in str_boards.split("\n"):
    if line != "":
        b.append(line.split())
    if line == "":
        if b:
            boards.append(b[:])
            b.clear()


def get_min_cols():
    last_index_in_col = list()

    for b in boards:
        indexs = list()
        for col in range(len(b)):
            index_of_last_item_will_get = 0
            for line in b:
                index_of_last_item_will_get = max(numbers.index(line[col]), index_of_last_item_will_get)
            indexs.append(index_of_last_item_will_get)
        last_index_in_col.append(indexs)
    #print("Last index in cols")
    #print(last_index_in_col)

    min_col = list()

    for board_num, l in enumerate(last_index_in_col):
        minVal = l[0]
        row = 0
        for line, val in enumerate(l):
            if val < minVal:
                minVal = val
                row = line
        min_col.append( (board_num, row, minVal) )

    return min_col


def get_min_rows():
    last_index_in_row = list()

    for b in boards:
        last_indexs = list()
        for l in b:
            last_index_in_line = 0
            for item in l:
                last_index_in_line = max(numbers.index(item), last_index_in_line)
            last_indexs.append(last_index_in_line)
        last_index_in_row.append(last_indexs)
    #print("Last index in rows")
    #print(last_index_in_row)

    min_row = list()

    for board_index, l in enumerate(last_index_in_row):
        minVal = l[0]
        row = 0
        for line, val in enumerate(l):
            if val < minVal:
                minVal = val
                row = line
        min_row.append((board_index, row, minVal))

    return min_row


min_col = get_min_cols()
min_row = get_min_rows()

#print("MinCol:")
#for l in min_col:
#    print(l)

#print("MinRow:")
#for l in min_row:
#    print(l)

final_list = list()
for i in range(len(boards)):
    if min_col[i][2] < min_row[i][2]:
        final_list.append(list(min_col[i]))
    else:
        final_list.append(list(min_row[i]))

print("Final List:")
for l in final_list:
    print(l)

print("\n\n\n")
print("Winner")
print("--------------------------------")
winner_board = 0
final_row = 0
final_number_index = 99999

for b_index, l_index, number_index in final_list:
    if number_index < final_number_index:
        winner_board = b_index
        final_row_col = l_index
        final_number_index = number_index

marked_numbers = numbers[:final_number_index+1]
#print(marked_numbers)

total = 0
for l in boards[winner_board]:
    # print(l)
    for item in l:
        if item not in marked_numbers:
            total += int(item)

print("Board: ", winner_board+1)
print(f"Total = {total} , numbers[{final_number_index}] = {numbers[final_number_index]}")
print("Result: ", total * int(numbers[final_number_index]))


print("\n")
print("Loser")
print("--------------------------------")

loser_board = 0
final_row = 0
final_number_index = 0

for b_index, l_index, number_index in final_list:
    if number_index > final_number_index:
        loser_board = b_index
        final_row_col = l_index
        final_number_index = number_index

marked_numbers = numbers[:final_number_index+1]
#print(marked_numbers)

total = 0
for l in boards[loser_board]:
    # print(l)
    for item in l:
        if item not in marked_numbers:
            total += int(item)

print("Board: ", loser_board+1)
print(f"Total = {total} , numbers[{final_number_index}] = {numbers[final_number_index]}")
print("Result: ", total * int(numbers[final_number_index]))
