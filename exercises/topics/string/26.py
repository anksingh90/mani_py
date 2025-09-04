str=input("Enter a string")
for i in str:
    if i in "aeiouAEIOU":
        print("#",end='')
    else:
        print(i,end='') 
print('')           
