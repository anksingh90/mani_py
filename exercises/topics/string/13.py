str=input("Enter a string")
count=0
def_count=0
for char in str:
    if char.isalpha():
        count=count+1
    elif char.isdigit():
        def_count=def_count+1
print("number of charter",count) 
print("number of digit", def_count)