# write menu given p to perfrom various operations 
# create a list with values 
# incert new values (lst.insert (pos,value))
# append an element
# modify/edit the existing value delete an exsting value from position (lst.pop(pos)) lst2=st1.posvalue,print(lst2)
# delete an exsting value from given value(lst.remove(value))
# sort the arry in ascending/decending order (lst.sort()),print(lst),(lst.sort(-1)==2),print(lst)

lst=[]
len_lst=int(input("Enter the length of the list : "))
for i in range (len_lst):
    val=int(input("Enter the value : "))
    lst.append(val) 

#menu driven program
while True:
    print("1. To insert new values")
    print("2. To append")
    print("3. To modify or edit the exsting list")
    print("4. Delete an exsting value from given value")
    print("5. Exit")
    ch=int(input("Enter your choice "))
    if ch==1:
        print('Values of list : ',lst)
        pos=int(input("Enter the position"))
        value=int(input("Enter the value to insert"))
        lst.insert (pos,value)
        print("updated list",lst)  
    elif ch==2:
        print(lst)
        val=int(input("Enter a value for append"))
        lst.append(val)
        print("updated list",lst)
    elif ch==3:
        print(lst)
        pos=int(input("Enter the position of the exting value to delete"))
        val=int(input("Enter the value to edit"))
        lst[pos]=val
        print("updated list",lst)
    elif ch==4:
        print(lst)    
        val=int(input("Enter the value to delete : "))
        lst.remove(val)
        print("updated list",lst)
    elif ch==5:
        break
    else:
        print('Invalid Response !')