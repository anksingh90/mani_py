#Write a program to separate the character and numeric values from a given list and store them in separate lists.
#Given list:
#A = [1, 'f', 2, 'b', 3, 4, 'h', 'j', 6, 9, 0, 'k']

A = [1, 'f', 2, 'b', 3, 4, 'h', 'j', 6, 9, 0, 'k']
num=[]
alpha=[]
for i in A:
    if str(i).isalpha():
        alpha.append(i)
    if str(i).isdigit():
        num.append(i)

print(num,alpha) 