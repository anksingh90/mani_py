count=0
a_count=0
str=input("Enter a string")
for i in str:
    if i.isalpha():
        count=count+1
    if i.isdigit():
        a_count=a_count+1

print(count)
print(a_count)    