#Count positive and negative numbers in a list.
count=0
count_=0
lst=[12,15,18,-12,-15,-18]
for i in lst:
    if i>0:
        count+=1
    elif i<0:
        count_+=1    
print(count)        
print(count_)