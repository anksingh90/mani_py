#school management system
while True:
    print("press1 to add student")
    print("press2 to display all students")
    print("press3 to search student")
    print("press4 to update student marks")
    print("press5 to delete student")
    print("press6 to show result summary")
    print("press7 to exit")
    ch=int(input("Enter your choice"))
    lst=[] # Global variable
    if ch==1: # accpt names of student !
        val = int(input("Enter number of entries for Student : "))
        for i in range(val):
            name=input("Enter name of students ")
            lst.append(name)
        print(lst)
    elif ch==2: # print the names of student in tabular format (lst)
        # using loop print all the values in list
        #  print('Option 2')
        print(lst)
        for i in range(len(lst)):
            print('Roll No : ',i,', Name :  ',lst[i])         
    elif ch==3:
        lst2=input("Enter name of the student to be searched from the above list") 
        print([lst2])
    elif ch==4:
        marks=float(input("Enter marks of the student"))    
        print(marks)
    elif ch==5:
        l=input("Enter name of the student to delete from the above list ")
        lst.remove(l)
        print(lst)
    #elif ch==6: