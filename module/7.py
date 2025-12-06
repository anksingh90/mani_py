lst = ['Liam ','Olivia ','Noah ','Emma ','Oliver ','Amelia ','Theodore ','Charlotte ','James ','Mia ']
stu={}
import random
for i in range(4):
    value=lst[i]
    keys=random.randint(1000,9999)
    stu[keys] = value
print(stu)