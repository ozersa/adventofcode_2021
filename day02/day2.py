import sys
from day2_1_input import *
from day2_2_input import *

cmd = list()

for line in s.split("\n"):
	if line == "":
		continue
	d, pos = line.strip().split()

	cmd.append( (d, int(pos)))


def process_question1():
	h = 0
	p = 0

	for s, pos in cmd:
	    if s == "forward":
	        h += pos
	    if s == "down":
	        p += pos
	    if s == "up":
	        p -= pos

	print("h", h)
	print("p", p)
	print("Q1 Answer (h*p): ", h*p)


def process_question2():
	h = 0
	p = 0

	aim = 0
	for s, pos in cmd:
	    if s == "forward":
	        h += pos
	        p += (aim * pos)
	    if s == "down":
	        #p += pos
	        aim += pos
	    if s == "up":
	        #p -= pos
	        aim -= pos

	print("h", h)
	print("p", p)
	
	print("Q2 Answer (h*p): ", h*p)



process_question1()
process_question2()
