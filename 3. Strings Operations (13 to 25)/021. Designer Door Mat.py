# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Sample Designs

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------
# Input Format

# A single line containing the space separated values of  and .

# Constraints

# Output Format

# Output the design pattern.

# Sample Input

# 9 27
# Sample Output

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

# **// 1st Method //**
n, m = map(int, input().split())

for line in range(1, (n//2 + 1)):
    design_num = (line*2-1)
    left_right_pattern = m - 3*design_num
    print("-"*(left_right_pattern//2) + ".|."*(design_num) + "-"*(left_right_pattern//2))

print("-"*((m-7)//2) + "WELCOME" + "-"*((m-7)//2))

for line in range(n//2, 0, -1):
    design_num = (line*2-1)
    left_right_pattern = m - 3*design_num
    print("-"*(left_right_pattern//2) + ".|."*(design_num) + "-"*(left_right_pattern//2))


# **// 2nd Method //**    
# n, m = map(int, input().split(' '))

if n%2 == 1 and m == 3*n:
    for i in range(1, (n//2 + 1)):
        design = ".|."*(i*2-1)
        pattern = design.center(m, "-")
        print(pattern)
    
    mid_design = "WELCOME"
    pattern = mid_design.center(m, "-")
    print(pattern)

    for i in range(n//2, 0, -1):
        design = ".|."*(i*2-1)
        pattern = design.center(m, "-")
        print(pattern)
