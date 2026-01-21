import random

print("**!!Welcome to Poker dice game!!**")
print("press 1 to play single round mode ")
print("press 2 to play multi round mode")
print("press 3 to exit")

ch=int(input("Enter your choice :"))
points=0
guess=[]
for i in range(0,5):
    value=random.randint(1,6)
    guess.append(value)
print(guess)

while True:
    round = 1 # checks the round of loop

    if ch==1:
        count={}
    for value in guess:
        count[value]=count.get(value,0)+1
    
    if set(guess)=={1} or set(guess)=={2} or set(guess)=={3} or set(guess)=={4} or set(guess)=={5} or set(guess)=={6}:
       print("current Hand:,Five of a Kind")
       points+=500
       print("potential Score:",points)
    
    elif 4 in count.values():
       print("current Hand:,Four of a Kind")
       points+=400
       print("potential Score:",points)
    
    elif 3 in count.values() and 2 in count.values():
        print("current Hand :,full house")
        points+=300
        print("potential score:",points) 
        break # remove this break
    elif 3 in count.values():
        print("current Hand :,Three of a kind")
        points+=150
        print("potential score:",points) 
        break # remove this break
    elif 2 in count.values() and 2 in count.values():
        print("current Hand :,two pair")
        points+=100
        print("potential score:",points) 
        break # remove this break
    elif 1 in count.values():
        print("current Hand :,one pair")
        points+=50
        print("potential score:",points) 
        break # remove this break
    '''
    if round == 3:
        break       
    else:
        round = round + 1
    '''