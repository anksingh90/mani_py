#ship cost calculator
print("Enter your destination")
print("press 1: Domestic")
print("press 2: Internationl")
ch=int(input("Enter your choice: "))
weight=float(input("Enter weight of the package in kg : "))
if ch==1:
    if weight>0 and weight<1:
        print("cost of transportation : $5")
    elif weight>=1 and weight<=5:
        print("cost of transportation : $10")    
    elif weight>5:
        print("cost of transportation : $15")            
elif ch==2:
    delivery=input("press1 : standard delivery \n press2 : express delivery : ")
    if weight>0 and weight<=1:
        print("cost of transportation : $15")
        print("express cost of transportation : $25 ")
    elif weight>=1 and weight<=5:
        print("cost of transportation : $30")
        print("express cost of transportation : $45")
    elif weight>5:
        print("express cost of transportation : $55")
else:
    print("Invalid")            
        



       