lst=[3,5,6,-3,-5,-6]
lst1=[]
lst2=[]
for i in lst:
    if i>=0:
        lst1.append(i)
    elif i<=0:
        lst2.append(i)  
print(lst)    
print(lst1)      
print(lst2)