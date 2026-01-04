# Program 7 : High Card Wins (Mini Project)

import random

print("***Welcome to High Card Wins Game***\n")

deck = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'JACK',12:'QUEEN',13:'KING',14:'ACE'}
sys_deck=[]
user_deck=[]
scoreofuser=0
scoreofsys=0

while True:         # generating system deck
    value=random.randint(2,14)
    if value not in sys_deck:
      sys_deck.append(value)
    if len(sys_deck)==5:
        break
    #print(sys_deck)

while True:     # generating user deck
    guess=random.randint(2,14)
    if guess not in user_deck:
        user_deck.append(guess)
    if len(user_deck)==5:
        break

# main game starts from here !

for round in range(5):
    # sys generating random card
    ch_sys = random.randint(0, len(sys_deck)-1)
    print("\nSystem : Shuffling Cards -")
    print('System has drawn its card.\n')

    # user generating random card
    print("\nUser : Shuffling Cards -")
    print('Available cards for you : ')

    for i in range(len(user_deck)):  # print user cards
        print('Card Position : ', i+1, ' Card :  ',deck[user_deck[i]])

    ch_user = int(input('Enter the card you want to play (enter position) : '))-1

    print(user_deck[ch_user])
    print(sys_deck[ch_sys])

    # comparision between user and system 
    if user_deck[ch_user] > sys_deck[ch_sys]:
        print('user wins')
    elif user_deck[ch_user] < sys_deck[ch_sys]:
        print('sys wins')
    elif user_deck[ch_user] == sys_deck[ch_sys]:
        print('draw')

    # result

    # remove cards played by user and system

# main final scoring 

