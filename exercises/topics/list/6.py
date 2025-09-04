lst=[1,1,2,2,3,3,4,4]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)        
