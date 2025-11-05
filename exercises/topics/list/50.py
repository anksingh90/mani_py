# write a menu driven program to input names of "n" no. of students,totl marks,avg marks,result and store them in 
# nested tuple with display the follwing menu
# 1.result "display name,marks,avg marks,(result p/f)"
# 2.display"display name,marks,avg marks"
# 3.search"search input name and display details of students
# 4. merit list display avg marks 70+,name
num=int(input("Enter total number of students : "))
stu = ()
stu1 = ()
for i in range(1, num+1):
    name = input("Enter name of student : ")
    t_marks=int(input("Enter total marks of each student for all subjects (Out of 500) : "))
    avg_marks = int(t_marks/5)
    if avg_marks>33:
        result = 'Pass'
    else:
        result = 'Fail'
    stu = (name,t_marks,avg_marks,result,)
    stu1 = stu1 + (stu,)


print(stu1)
print("1.result") 
print("2.display") 
print("3.search")  
print("4.merit list")
ch=int(input("Enter your choice"))
if ch==1:
    print(stu)
elif ch==2:
    print("name",t_marks,avg_marks)
elif ch==3:
    print(stu)
elif ch==4:
    if avg_marks>70: 
        print("name")  
else:
    print("invalid input")         
    

