"""
Write a program to create a game, roll a dice. every time game rolls a dice, user need to predict the number. If 
numbers entered by user is same as of dice then respond - number is
 correct else incorrect. total of 5 chances, if user gets 3 correct prediction, user wins the games else loses the game.
"""
import random
print("***welcome to game roll a dice***")
count=0
for i in range(6):
    guess=random.randint(1,6)
    num=int(input("Enter number for a dice"))
    if guess==num:
        print("correct")
        count+=1
        if count==3:
            break
    else:
        print("incorrect")    

