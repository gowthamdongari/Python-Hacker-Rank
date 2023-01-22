# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains n. The second line contains an array A[i]  of  integers each separated by a space.

# Constraints
# 2<=n<=10
# -100<=a[i]<=100
# Output Format

# Print the runner-up score.

# Sample Input 0

# 5
# 2 3 6 6 5
# Sample Output 0

# 5

n = int(input())
arr = map(int, input().split(" "))
if 2<=n<=10:
    new_arr = [x for x in arr if -100 <= x <= 100]
    max_2_num = sorted(set(new_arr))[-2]
    print(max_2_num)



