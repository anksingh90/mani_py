lst=[]
import random
val=[]
for i in range(100):
    val=random.randint(1,50)
    if val%2==0:
        lst.append(val)
    if len(lst)==5:
        break
print(lst)