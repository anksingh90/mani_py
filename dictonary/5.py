# wap to input names of n customers/items and  cost ,phne no..store it in a dict and display all details in tabular form.
stu={}
num=int(input("Enter the total number of customers"))
for i in range(num):
    names=input("Enter names of the customers : ")
    items=input("Enter name of the items purchased : ")
    cost=int(input("Enter the cost of items purchased by them"))
    stu[names]=[items,cost]

print('name \t items \tcost')
for keys, values in stu.items():
    print(keys,'\t', end =' ')   
    for j in values:
        print(j,'\t',end ='')
    print()