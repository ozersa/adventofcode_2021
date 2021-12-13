import sys
#from day2_1_input import *
from day2_2_input import *

h = 0
p = 0

aim = 0
for s, pos in l:
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
print("h*p", h*p)
