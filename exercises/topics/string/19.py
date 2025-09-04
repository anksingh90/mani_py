count=0
a_count=0
sum=0
str=input("Enter a string")
for i in str:
    if len(str):
        count=count+1
    if i.isalpha():
        a_count=a_count+1
    if i.isdigit():
        sum=sum+1
print(count)        
print(a_count)
print(sum)

