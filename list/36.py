# Write a program to read a list of elements. 
# Modify this list so that it does not contain any duplicate elements, i.e., 
# all elements occurring multiple times in the list should appear only once.

lst=[1,1,2,2,3,3,4,4]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)