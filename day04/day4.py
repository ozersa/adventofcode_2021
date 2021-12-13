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
