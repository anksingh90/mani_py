"""
Write a program to create a game, roll a dice. every time game rolls a dice, user need to predict the number. If 
numbers entered by user is same as of dice then respond - number is
 correct else incorrect. total of 5 chances, if user gets 3 correct prediction, user wins the games else loses the game.
"""
import random
print('**** welcome to game roll a dice ****')
count=0
for i in range(6):
    # generating a new number for guess
    guess = random.randint(1,6)
    num=int(input("Guess the number : "))
    if guess == num :
        print("number is correct")
        # create a mechnism to record the correct guess
        count+=1
        # only 3 correct guess shuold be recored !
        if count==3:
            print("you wins")
            break
    else:
        print("incorrect")    
