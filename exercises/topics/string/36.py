# wap to input a string and replace blank space with#.
# output : Enter#a#string
str=input("Enter a string : ")
for i in str:
    if i==" ":
        print("#",end="")
    else:
        print(i,end='')    