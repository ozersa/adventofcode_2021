import sys
from day8_1_input import *
from day8_2_input import *

#str_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

def process_question1():
    total_1_4_7_8 = 0
    for line in str_input.split('\n'):
        if line == "":
            continue
        digits, segments = line.split('|')
        for item in segments.split():
            if len(item) in (2, 3, 4, 7):
                total_1_4_7_8 += 1

    print("Number of 1-4-7-8: ", total_1_4_7_8)


def process_question2():
    total = 0
    for line in str_input.split('\n'):
        if line == "":
            continue
        digits, segments = line.split('|')
        l = sorted(digits.strip().split(), key=len)
        #print("Sorted list: ", l)
        digits = list(range(10))

        digits[1] = l[0]
        digits[4] = l[2]
        digits[7] = l[1]
        digits[8] = l[9]

        five_digits = l[3:6]
        six_digits = l[6:9]

        for item in six_digits:
            if not (set(digits[1]) < set(item)):
                digits[6] = item
            elif set(digits[4]) < set(item):
                digits[9] = item
            else:
                digits[0] = item

        item_2_and_5 = list()
        for item in five_digits:
            if set(digits[1]) < set(item):
                digits[3] = item
            else:
                item_2_and_5.append(item)

        if (set(item_2_and_5[1]) | set(digits[1]) ) == set(digits[9]):
            digits[2], digits[5] = item_2_and_5[0], item_2_and_5[1]
        else:
            digits[2], digits[5] = item_2_and_5[1], item_2_and_5[0]

        val = 0
        for item in segments.strip().split():
            for index, signal in enumerate(digits):
                if set(signal) == set(item):
                    val *= 10
                    val += index
                    break

        #print("Val: ", val)
        total += val
    print("Q2 Total: ", total)

process_question1()
process_question2()
