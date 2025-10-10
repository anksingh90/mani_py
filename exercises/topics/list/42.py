#Find second largest number using:
#Method 1: Using loop
#Method 2: Using sort()
#for largest number and second largest

lst=[45,50,65,55]


count=0
for i in lst:
    if i>=count:
        count=i
        sum=(count)
    elif i<=0:
        continue   
print(i)
print(count)


