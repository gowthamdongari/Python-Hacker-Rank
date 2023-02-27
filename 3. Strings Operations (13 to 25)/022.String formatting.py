# Given an integer, , print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# Function Description

# Complete the print_formatted function in the editor below.

# print_formatted has the following parameters:

# int number: the maximum value to print
# Prints

# The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

# Input Format

# A single integer denoting .

# Constraints

# Sample Input

# 17
# Sample Output

#     1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001


def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))

    for i in range(1, number + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# 'd' Signed integer decimal.  
# 'i' Signed integer decimal.  
# 'o' Signed octal value. (1)
# 'u' Obsolete type – it is identical to 'd'. (7)
# 'x' Signed hexadecimal (lowercase). (2)
# 'X' Signed hexadecimal (uppercase). (2)
# 'e' Floating point exponential format (lowercase).  (3)
# 'E' Floating point exponential format (uppercase).  (3)
# 'f' Floating point decimal format.  (3)
# 'F' Floating point decimal format.  (3)
# 'g' Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.  (4)
# 'G' Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.  (4)
# 'c' Single character (accepts integer or single character string).   
# 'r' String (converts any Python object using repr()).   (5)
# 's' String (converts any Python object using str()).    (6)
# '%' No argument is converted, results in a '%' character in the result.