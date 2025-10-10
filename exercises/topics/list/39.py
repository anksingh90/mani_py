lst=[0.2,0.3,0.4,2,3,4]
lst1=[]
lst2=[]
for i in lst:
    if i==int(i):
        lst1.append(i)
    elif i==float(i):
        lst2.append(i)    
print(lst)        
print(lst1)
print(lst2)