# ** Program 7 : High Card Wins (Mini Project) ** 
import random

print("*** Welcome to a game High Cards Wins ***")
deck = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'JACK',12:'QUEEN',13:'KING',14:'ACE'}
print('1. Single Round Game')
print('2. Multi Round Game (Best of 5)')
print('0.TO Exit')

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
    
    print('--- User : --- ')
    print('Available cards for you :')

    for i in range(5):
        print('Position : ' ,i+1, ' Card : ', deck[user_lst[i]])
    ch = int(input("Enter the card you want to play : ")) - 1
    
    print( "user card:", deck[user_lst[ch]])
    print("system card:",deck[sys_guess])

    if deck[user_lst[ch]]>deck[sys_guess]:
        print("user wins")
    else:
       print("system wins")

elif ch==2:
    print("***Multi Round Game***")
    scoreofuser=0
    scoreofsys=0
    for i in range(5):
        deck = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'JACK',12:'QUEEN',13:'KING',14:'ACE'}
        print("--- Round  ",i+1, ': ---')
        sys_deck=random.randint(2,14)
        print("\nSystem has drawn its card\n")
        print("User : Shuffling Cards ") 
        print("Available cards for you :")
        user_deck=[]
        while True:
            value=random.randint(2,14)
            if value not in user_deck:
               user_deck.append(value)
            if len(user_deck) == 5: 
                break

        for i in range(5):
            print("Position :",i+1,"card value",deck[user_deck[i]])
        ch= int(input("Enter the card you want to play (enter position) : "))
        print("\nuser :", deck[user_deck[ch-1]])
        print("system :", deck[sys_deck])

        print("Result:")
        print("Score after Round", i+1)
        if deck[user_deck[ch-1]]>deck[sys_deck]:
            print("**user wins**")
            scoreofuser+=1
        else:
            print("**system wins**")
            scoreofsys+=1 
print( "**userscore***",scoreofuser)
print( "***sysscore***",scoreofsys)  

if scoreofuser>scoreofsys:
    print("user wins the game!!")
elif scoreofuser==scoreofsys:
    print("draw")
else:
    print("system wins the game!!")    