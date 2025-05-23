print('press 1:area of square')
print('press 2:area of rectangle')
print('press 3:area of circle')
ch=input("Enter your choice : " )
print(ch)
if ch==1:
   a= ("Enter side of a square : ")
   b=("a**2")
   print(b)
elif ch==2:
   c=("Enter lenght of rectangle")
   d=("Enter the breadth of rectangle")  
   e=("l*b") 
   print(e)
elif ch==3:
   g=("Enter radius of a circle") 
   h=("3.14*g*g") 
   print(g) 
else:
   print("invalid")
