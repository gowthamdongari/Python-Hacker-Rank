# Given the names and grades for each student in a class of  students, store them in a nested list
#  and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically
#  and print each name on a new line.

# Example
# records = [["chi",20.0],["beta",50.0],["alpha",50.0]]

# The ordered list of scores is , so the second lowest score is . 
# There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta

# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints
# 2<=n<=5

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output 0

# Berry
# Harry

length_of_nest_list =int(input())
    if 2<=length_of_nest_list<=5:
        list_a = []
        scores_list = []
    for i in range(length_of_nest_list):
        name = input()
        score = float(input())
        list_a.append([name, score])
        scores_list.append(score)

    second_lowest = sorted(set(scores_list), reverse=True)[-2]
    list_a = sorted(list_a, key=lambda i:i[0])
    for i in range(length_of_nest_list):
        if list_a[i][1] == second_lowest:
            print(list_a[i][0])