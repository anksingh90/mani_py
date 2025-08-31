# Write a Python script to input a number and count the occurrences of that number in a given list.

count=0
list1 = [10, 20, 30, 40, 10, 50, 10]
print('List with values : ',list1)
num=int(input("Enter a number : "))
for i in list1:
    if num == i:
        count+=1

print(count)