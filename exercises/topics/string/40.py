#Write a program that reads a line then counts how man times a substring 'is/ appears in the line and displays the count.
count=0
str=input("Enter a string")
for i in str.split():
    if "is" == i:
        count+=1
print(count,end="")
