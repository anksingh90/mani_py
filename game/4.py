import random

print("**!!Welcome to Poker dice game!!**")
print("press 1 to play single round mode ")
print("press 2 to play multi round mode")
print("press 3 to exit")

ch=int(input("Enter your choice :"))
points=0
guess=[3, 3, 3, 3, 5]

for i in range(0,5):
    value=random.randint(1,6)
    guess.append(value)
print(guess)

if ch==1:
    count={}
    for value in guess:
        count[value]=count.get(value,0)+1
    
    if set(guess)=={1} or set(guess)=={2} or set(guess)=={3} or set(guess)=={4} or set(guess)=={5} or set(guess)=={6}:
       print("current Hand:,Five of a Kind")
       points+=500
       print("potential Score:",points)
    
    elif 4 in count.values():
       print("current Hand:,Five of a Kind")
       points+=400
       print("potential Score:",points)
       

    elif guess[0]==guess[1]==guess[2] or guess[2]==guess[3]==guess[4]:
        print("points :",400)
        print("do you want to re-rolls your dice","yes" or "no")
        pos=int(input("Enter position you want to re-rolls "))
        print("Re-rolls of dice",pos)
        guess1=random.randint(1,6)
        print("position",pos,"dice :",guess1)
        guess[pos].append(guess1)

    elif guess[0]!=guess[1]!=guess[2]!=guess[3]!=guess[4]:
        print("points :",0)
    