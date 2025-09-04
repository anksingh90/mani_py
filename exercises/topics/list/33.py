# a program to calculate avg marks of n students using a func. where n is entered by user

def avg_marks(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    avg_marks = sum/len(lst)
    print('Avg marks : ', avg_marks)


#main prog.
value = int(input('Enter the number of students : '))
marks=[]
for i in range(value):
    mark = int(input('Enter the marks for student :'))
    marks.append(mark)
print('List of numbers entered : ', marks)
avg_marks(marks)