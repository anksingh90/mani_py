count=0
tup=(1,2,2,3,4,4,5,5,6)
lst=[]
for i in tup:
    if i not in lst:
        print("value:",i,"is",tup.count(i),"times")
        lst.append(i)