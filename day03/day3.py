import sys
#from day3_1_input import *
from day3_2_input import *


l = list(s.split('\n'))

num_of_bits = len(list(l[0]))

print("-------------------------------")
print("OXYGEN")

for i in range(num_of_bits):
    num1 = 0
    num0 = 0

    l0 = list()
    l1 = list()

    #print("New L Size: ", len(l))
    #print(l)
    index = 0
    end = len(l)
    if end < 2:
        print(l)
    while index < end:
        line = l[index]
        if '0' == line[i]:
            num0 += 1
            l0.append(line)
        else:
            l1.append(line)
            num1 += 1
        index += 1
    if num1 >= num0:
        l = l1[:]
    else:
        l = l0[:]
print(l)

print("-------------------------------")
print("Co2")

l = list(s.split('\n'))

for i in range(num_of_bits):
    num1 = 0
    num0 = 0

    l0 = list()
    l1 = list()

    #print("New L Size Co2: ", len(l))
    #print(l)
    index = 0
    end = len(l)
    if end < 2:
        print(l)
    while index < end:
        line = l[index]
        if '0' == line[i]:
            num0 += 1
            l0.append(line)
        else:
            l1.append(line)
            num1 += 1
        index += 1
    if num1 < num0:
        l = l1[:]
    else:
        l = l0[:]
print(l)

