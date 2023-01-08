# You are given three integers  and  representing the dimensions of a cuboid 
# along with an integer n. Print a list of all possible coordinates given by 
# (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. 
# Here, 0<i<x; 0<j<y; 0<k<z; . Please use list comprehensions rather than multiple loops, 
# as a learning exercise.

# Example
# x = 1
# y = 1
# z = 2
# n = 3

# All permutations of [i,j,k] are:
# [0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2] .....

# Print an array of the elements that do not sum to n =3.
# i.e i+j+k should not be equal to n

# Input Format

# Four integers x,y,z and n, each on a separate line.

# Constraints
# Print the list in lexicographic increasing order.

# Sample Input 0

# 1
# 1
# 1
# 2
# Sample Output 0

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Explanation 0

# Each variable  and  will have values of  or . All permutations of lists in the form .
# Remove all arrays that sum to  to leave only the valid permutations.

x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
list_a = []    
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            permutations = [i, j, k]
            sum_of_variables = i+j+k
            if sum_of_variables!=n:
                list_a.append(permutations)
print(list_a)