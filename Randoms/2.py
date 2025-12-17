# Number Quest Function
# lst = [ 11,22,33,44,55,66,77 ]
# print the list values to user and ask user to guess a random number picked by the program.
# if user guess is correct, then add value in a list. then print in the end number of correct/incorrect guess.

import random
lst = [ 11,22,33,44,55,66,77 ]
score=[]
print("List values : [ 11,22,33,44,55,66,77 ]")
num=int(input("Guess number from the above given list :"))
guess=random.randrange(0,6) # picks index value 
print('Number picked by System : ',lst[guess])
if num==lst[guess]:
    print("guess is correct")
    score.append(1)
    print(score)
else:
    print("guess is incorrect")