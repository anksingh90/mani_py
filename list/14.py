'''
Write a Python program that performs the following tasks:

1. Asks the user to enter the number of students in a class.
2. Accepts the marks of each student and stores them in a list.
3. Prints the entered marks of all students.
4. Asks the user to delete the marks of a specific student by entering the student number.
5. After deleting the marks, prints the updated list of marks.
'''
num=int(input("Enter number of students marks to be entered"))
lst=[]
for i in range(num):
    marks=int(input("Enter marks of the student : "))
    lst.append(marks)

print("Entered marks are :",lst) 
r=int(input("Enter the marks you want to remove "))
lst.remove(r)
print("Updated Marks : ", lst)




