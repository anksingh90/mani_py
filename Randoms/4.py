import random
print("*** Welcome to a game roll a dice ***")
count=0
count_=0
for i in range(2):
    print("computer is rolling a dice")
    guess=random.randint(1,6)
    print(guess)
    print("do you want to roll a dice")
    print("yes")
    guess1=random.randint(1,6)
    print(guess1)
    if guess==guess1:
        print("match is draw")
    elif guess>guess1:
        print("computer wins")
        count_+=1
        print("computer score status is",count_)
    elif guess<guess1:
        print("user wins")
        count+=1
        print("user score status is",count)
    print("*********")
    print('###**** Score Card : ****###') 
    print("computer:",count_)
    print("user:",count)
    print("*********")