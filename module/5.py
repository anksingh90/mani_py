# randomly pick 4 names from the list and print it, if name is already printed then it needs to escape the value 
import random
val=[]
lst = ['Liam ','Olivia ','Noah ','Emma ','Oliver ','Amelia ','Theodore ','Charlotte ','James ','Mia ']
for i in range(0,4):
    num=random.randint(0,len(lst)-1)
    print(lst[num],end=' ,')
    if val in lst:
        continue
    else:
        print(lst[num],end=',')