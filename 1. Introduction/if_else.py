# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.


import math
import os
import random
import re
import sys



n = int(input())
if 1<=n<=100:
    if n%2 == 1 or 6<=n<=20:
        print('Weird')
    elif n%2 == 0:
        if 2<=n<=5 or n>20:
            print('Not Weird')
else:
    pass