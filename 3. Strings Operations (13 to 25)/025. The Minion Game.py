""" Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12"""

def minion_game(word):
    Stuart_score = 0
    Kevin_score = 0
    vowels = 'AEIOU'
    for i in range(len(word)):
        if word[i] in vowels:
            Kevin_score += (len(word) - i)
        else:
            Stuart_score += (len(word) - i)

    if Stuart_score > Kevin_score:
        name = "Stuart"
        score = str(Stuart_score)
        res = name + " " + score
    elif Stuart_score == Kevin_score: 
        res = "Draw"
    else:
        name = "Kevin"
        score = str(Kevin_score)
        res = name + " " + score
    print(res)
    
s = input()
minion_game(s)    



"""Normal step by step Method"""
def minion_game(word):
    Stuart_score = 0
    Kevin_score = 0
    vowels = ("A", "E", "I", "O", "U")
    word_list = []
    for i in range(len(word)):
        for j in range(1, len(word)+1):
            #substring formed with each letter as starting letter of a new word formed
            sub_word = word[i:j]
            word_list.append(sub_word)
    # print(word_list)        
    # set removes duplicates, filter removes empty strings in list
    set_word_list = set(list(filter(None, word_list))) 
    #score based on consonant or vowel starting letter 
    for item in set_word_list:
        if item[0] not in vowels:
            word_count_score = word_list.count(item)
            Stuart_score += word_count_score
        else:
            word_count_score = word_list.count(item)
            Kevin_score += word_count_score
    # printing the winner Score and name 
    if Stuart_score > Kevin_score:
        name = "Stuart"
        score = str(Stuart_score)
        res = name + " " + score
    elif Stuart_score == Kevin_score: 
        res = "Draw"
    else:
        name = "Kevin"
        score = str(Kevin_score)
        res = name + " " + score
    print(res)
    
s = input()
minion_game(s)    