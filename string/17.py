str="hello world"
a=input("Enter the number of times character occurs in a str")
i = 0
count=0
while i<=len(str)-1:
    if a == str[i]:
        count = count +1
    i=i+1
print(count)