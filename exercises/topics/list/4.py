# create a list of tuple with their numbers and their cubes
# [(1,1),(2,8),(3,27),(4,64)] #output
lst=[]
for i in range(1,56,1):
    lst.append ((i,i**3))
print(lst)    
