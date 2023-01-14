# You are given a string and your task is to swap cases. In other words, convert 
# all lowercase letters to uppercase letters and vice versa.

# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# Function Description

# Complete the swap_case function in the editor below.

# swap_case has the following parameters:

# string s: the string to modify

# Returns
# strings:

# string: the modified string
# Input Format

# A single line containing a string .

# Constraints
#  0<=len(s)<=1000

# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    swap_case = ""
    for i in s:
        if i.isupper():
            swap_case = swap_case + i.lower()
        elif i.islower():
            swap_case = swap_case + i.upper()
        else:
            swap_case = swap_case + i
    return swap_case


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)