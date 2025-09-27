#Write a Python program to count the number of digits, letters, and special characters in a given string.
count=0
count_=0
sum=0
str=input("Enter a string")
for i in str:
    if i.isdigit():
        count+=1
    elif i.isalpha():
        count_+=1
    elif "@#$%&*" in i:
        sum+=1
print(count)       
print(count_) 
print(sum)               