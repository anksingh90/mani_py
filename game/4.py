import random

print("*****  Welcome to Poker dice game  *****")
print("Press 1 : Play single round mode ")
print("Press 2 : Play multi round mode")
print("Press 3 : Exit")

ch=int(input("Enter your choice : "))
points=0
guess=[]

'''
lst = [1,2,3]
print('Position : 1\t 2\t 3\t')
print('Values   :',lst[0],'\t',lst[1],'\t',lst[2])
'''

for i in range(0,5):
    value=random.randint(1,6)
    guess.append(value)

print('Position:  0   1   2   3   4')
print(' dice :   ' ,   guess)       

while True:
    round = 1
    print('Round : 1')
    if ch==1:       
        count={}   
        for value in guess:
            count[value]=count.get(value,0) + 1
    
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
            
        elif 3 in count.values():
            print("current Hand :,Three of a kind")
            points+=150
            print("potential score:",points) 
            
        elif 2 in count.values() and 2 in count.values():
            print("current Hand :,two pair")
            points+=100
            print("potential score:",points) 
            
        elif 1 in count.values():
            print("current Hand :,one pair")
            points+=50
            print("potential score:",points) 
        
        print("Re-rolls remaining :",round-3)
        print("**!!**")

        ch=input("Keep this hand or try to improve? (Y to keep, N to re-roll): ").lower()
        if ch=='n':
            n_pos = int(input('Enter number of position to be re-rolled : (1/2/3/4) '))
            
            for i in range (n_pos):
                print('Enter',i+1,'position value to be re-rolls :', end=' ')
                pos=int(input())-1
                value=random.randint(1,6)
                guess[pos]=value
            print(guess)
        else:
            print("want to keep this hand")
            break
    if round == 3:
        break       
    else:
        round = round + 1
    
