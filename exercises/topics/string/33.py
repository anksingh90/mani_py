#wap to remove "i" from string
str=input("Enter the string")
for a in str:
    if "i" not in a:
        print(a,end="")
    else:
        continue    