#Write a program that reads a sting and then prints a string that capializes every other letter in the string. 
# eg. school becomes sChOoL.
str=input("Enter a string")
for i in range(len(str)):
    if i%2==0:
        print(str[i].upper(),end="")
    else:
        print(str[i],end='')    
    