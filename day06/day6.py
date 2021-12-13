import sys
from day6_1_input import *
from day6_2_input import *


s = "3,4,3,1,2"

total_days= 18
fish_start = [int(x) for x in s.split(",")]

#multiply = [125, 44, 48, 40, 43]
multiply = list()

for i in range(7):
    multiply.append(fish_start.count(i))
    print(f"Count {i} : {fish_start.count(i)}")

current_fish = len(fish_start)
for day in range(total_days):
    for i in range(current_fish):
        if fish_start[i] == 0:
            fish_start[i] = 6
            fish_start.append(8)
            current_fish += 1
        else:
            fish_start[i] -= 1

print("Total Fish: ", len(fish_start))
