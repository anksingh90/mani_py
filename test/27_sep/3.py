#Write a program that interactively creates a nested list to store the marks in three subjects.
#  for five students. The list will look like:
#Marks = [[45,45,40], [35,40,38], [36,30,38], [25,27,20], [10,15,20]]
marks1=[]
sum = 0
for i in range(2):
    val1 = input('Enter a value : ')
    val2 = input('Enter a value : ')
    val3 = input('Enter a value : ')
    marks1.append([val1,val2,val3])
for i in marks1:
    for j in i:
        sum = sum + j
    print("mean",int(sum/len(i))) 