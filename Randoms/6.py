# rock paper 
import random
print("*** welcome to game ***")
lst=["rock,paper,scissor"]
for i in range(5):
   guess=random.randint(0,3)
   print(guess)
   guess1=random.randint(0,3)
if lst[0]==lst[0]:
      print("draw")
elif lst[0]>lst[1]:
     print("paper wins")
elif lst[0]>lst[2]:
     print("scissor wins")
elif lst[1]>lst[2]:
     print("scissor wins")     
elif lst[1]==lst[1]:
     print("draw") 
elif lst[2]>lst[2]:
     print("draw")  
elif lst[2]>lst[1]:
     print("scissor wins")   
elif lst[2]>lst[0]:
     print("rock wins")
