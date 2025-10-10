#Given lst = [10, 'fun', 20, 'World', 30, 'home'], create a new list where numbers are replaced with their cubes.
lst=[10, 'fun', 20, 'World', 30, 'home']
for i in lst:
    if type(i)==int:
        print(i**3,end="")
    elif type(i)==str:
        print(i,end="")  
         