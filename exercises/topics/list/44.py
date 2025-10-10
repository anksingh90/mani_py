#Create a nested list to store roll number, name, and marks of students.
roll_number= int(input("Enter your roll number"))
name=input("Enter your name")
marks=float(input("Enter your marks"))
lst=[]
lst1=[]
lst2=[]
list=[]
lst.append(roll_number)
lst1.append(name)
lst2.append(marks)
list=lst+lst1+lst2
print(list)