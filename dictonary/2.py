# dictionary declaration (key : roll_No, Value : [Name, Class, Marks 1, Marks 2, Marks 3])
stu = { 101:[ 'abc', 11, 70, 60, 55 ],102:["xyz",11,89,98,78]}
stu1=[]
while True:
# Create menu driven loop
    print("press1 to add student")
    print("press2 to display all students")
    print("press3 to search student")
    print("press4 to update student marks")
    print("press5 to delete student")
    print("press6 to show result summary")
    print("press7 to exit")
    ch=int(input("Enter your choice"))
# Declare each sub-programs as per Menu
    if ch==1:
        num=int(input("Enter the number of entries"))
        for i in range(num):
            roll_no = int(input('Enter your roll_no : '))
            name=input("Enter name of student to be added : ")
            clss=int(input("Enter your class"))
            marks1=int(input("Enter your marks of physics "))
            marks2=int(input("Enter your marks of maths "))
            marks3=int(input("Enter your marks of chemistry "))
            stu[roll_no] = [name,clss,marks1,marks2,marks3]
        print(stu)
    elif ch==2:
        for keys,values in stu.items():
            print(keys,end='')
            print(values)
    elif ch==3:
        print('Roll_No \t Name \t Class \t Sub1 \t Sub2 \t Sub3')
        for keys,values in stu.items():
            print(keys ,end='\t\t')
            for j in values:
                print(j, end=' \t')
            print(' ')
        
        roll_no=int(input('Enter your roll_no to be searched: '))   
        print('Student Details : ',stu.get(roll_no))
    elif ch==4: # update marks of student
        print(stu)
        roll_no = int(input('Enter roll no of student : '))
        value = stu.get(roll_no)
        marks = int(input('Enter marks : '))
        value[2] = marks
        stu[roll_no] = value
        print(stu)

    elif ch==5:
        roll_no=int(input("Enter roll_no of student to be delete"))
        stu.pop(roll_no)
        print(stu)
    elif ch==6:
        print('exit') 