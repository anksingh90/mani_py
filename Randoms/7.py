# ** Program 7 : High Card Wins (Mini Project) **

import random

print("*** Welcome to a game High Cards Wins ***")
deck = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'JACK',12:'QUEEN',13:'KING',14:'ACE'}
print('1. Single Round Game')
print('2. Multi Round Game (Best of 5)')
ch=int(input("Enter your choice : "))

if ch==1:
    print("** Single Round Mode **")

    # system : selecting 1 card randomly
    sys_guess=random.randint(2,14)
    print("System has drawn its card")

    # user : randomly selecting 5 cards from deck
    user_lst=[]
    while True:
        card = random.randint(2,14) # duplicacy
        if card not in user_lst:
            user_lst.append(card) # adding cards to user list.
        if len(user_lst) == 5:
            break
    
    print('User : ')
    print('Available cards for you :')
    for i in range(5):
        print(deck[user_lst[i]], end = ', ')
    print(' ')

    # comparing if user wins or system !


    # print the output !

