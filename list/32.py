# write menu given p to perfrom various operations 
# create a list with values 
# incert new values (lst.insert (pos,value))
# append an element 
# modify/edit the exsteing value delete an exsting value from position (lst.pop(pos)) lst2=st1.posvalue,print(lst2)
# delete an exsting value from given value(lst.remove(value)) 
# sort the arry in ascending/decending order (lst.sort()),print(lst),(lst.sort(-1)==2),print(lst)
lst=[]
len_lst=input("Enter the length of the list ")
for i in range (len(len_lst)):
    val=input("Enter the value for list")
    lst.append(val)   

#menu driven program
while True:
    print("1.to insert new values")
    print("2. to append")
    print("3.to modify or edit the exsting list")
    print("4.delete an exsting value from given value")
    print("5.exit")
    ch=int(input("Enter your choice "))
if ch==1:
    print(lst)
    pos=int(input("Enter the position of a list))
    print(lst.insert(pos))    
elif ch==2:
    print(lst)
    val=int(input("Enter a value for append"))
    print(lst.append(val))  
#elif ch==3:
    #print(lst)
