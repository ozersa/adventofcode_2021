import sys
from day7_1_input import *
from day7_2_input import *

"""

Solution for Question 1

"""
def process_question1():
    total_fuel = list()

    loop_count = len(positions)
    for i in range(loop_count):
        distance = 0
        for j in range(loop_count):
            distance += abs(positions[i] - positions[j])
        total_fuel.append(distance)

    print("Question 1")
    print("Min feul consumption: ", min(total_fuel))


"""

Solution for Question 2

"""
def process_question2():
    total_fuel = list()

    averages = list()
    average = round(sum(positions) / len(positions))

    averages.append(average)
    averages.append(average-1)

    for average in averages:
        total = 0
        for pos in positions:
            t = abs(pos - average)
            t = (t * (t+1)) // 2
            total += t
        total_fuel.append(total)

    index = total_fuel.index(min(total_fuel))

    print("Question 2")
    print(f"Point: {averages[index]}  Fuel Consumption: ", total_fuel[index])


process_question1()
process_question2()
