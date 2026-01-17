import random

#Hand Distribution:
#Full House: 2 (40%)
#Straight: 1 (20%)
#Three of a Kind: 1 (20%)
#One Pair: 1 (20%)

print("**!!Welcome to Poker dice game!!**")
print("press 1 to play single round mode ")
print("press 2 to play multi round mode")
print("press 3 to exit")

ch=int(input("Enter your choice :"))
points=[]
guess=[]
if ch==1:
    print("Rolling 5 dice..")
    for i in range(5):
        value=random.randint(1,6)
        guess.append(value)
    
    # printing the dice list
    '''
    Position:  0   1   2   3   4
    Dice:     [2] [4] [2] [6] [2]
    '''
    print(guess)

    # compare or check if any index is mataching !

    if guess[0]==guess[1] or guess[1]==guess[2] or guess[2]==guess[3] or guess[3]==guess[4] or guess[4]==guess[0]:
        print(" JACKPOT! FIVE OF A KIND!")
        print("points :",500)
        print("do you want to Re-rolls your dice","yes" or "no")
    elif guess[0]!=guess[1] or guess[1]!=guess[2] or guess[2]!=guess[3] or guess[3]!=guess[4] or guess[4]!=guess[0]:  
        print("points :",150)
        print("do you want to re-rolls your dice","yes" or "no")
        pos=int(input("Enter position you want to re-rolls "))
        print("Re-rolls of dice",pos)
        guess1=random.randint(1,6)
        print("position",pos,"dice :",guess1)
    elif guess[0]!=guess[1]!=guess[2] or guess[2]!=guess[3]!=guess[4]:
        print("points :",400)
        print("do you want to re-rolls your dice","yes" or "no")
        pos=int(input("Enter position you want to re-rolls "))
        print("Re-rolls of dice",pos)
        guess1=random.randint(1,6)
        print("position",pos,"dice :",guess1)
        guess[pos].append(guess1)

    elif guess[0]!=guess[1]!=guess[2]!=guess[3]!=guess[4]:
        print("points :",0)
    