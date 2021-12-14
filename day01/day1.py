import sys
from day1_1_input import *
from day1_2_input import *

numbers=list()
for line in s.split("\n"):
	if line == "":
		continue
	numbers.append(int(line))


def process_question1():
	counter = 0
	k = 0
	for i in numbers[1:]:
	    if i > numbers[k]:
	        counter += 1
	    k += 1

	print("Q1 Answer: ", counter)


def process_question2():
	l = list()
	for i in range(0, len(numbers)-2):
	    a = numbers[i] + numbers[i+1] + numbers[i+2]
	    #print(a)
	    l.append(a)
	    

	counter = 0
	k = 0
	for i in l[1:]:
	    if i > l[k]:
	        counter += 1
	    k += 1
	
	print("Q2 Answer: ", counter)



process_question1()
process_question2()
