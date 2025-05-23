#wap to simuluate atm machine atm should provide following options to user: 
#1=check balance 2=deposit 3=withdraw 4=exit
#account balance =10000
print("press 1: total balance :")
print("press 2: deposit : ")
print("press 3:  withdraw : ")
print("press 4:  exit")
ch=int(input("Enter your choice"))
if ch==1:
    print("10000")
elif ch==2:
    a=int(input("Enter the value deposit"))
    print(10000+a)
elif ch==3:
    b=int(input("Enter the value withdraw"))
    print(10000-b)  
else:
    print("invalid response") 




23/5         