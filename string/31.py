# Write a python program to enter a string from the user and perform the following tasks and print the result after all operations:
#(i)   Count the number of alphabets present in the string
#(ii)  Count the number of vowels present in the string
#(iii) Count the number of spaces present in the string

str=input("Enter a string")
count=0
count_=0
add=0
for i in str:
    if i.isalpha():
        count = count+1
    if i in "aeiouAEIOU":
        count_=count_+1
    if i.isspace():
        add=add+1    
print(count) 
print(count_)   
print(add)
