# Write a user-defined function to check if a number is present in the list or not. 
# If the number is present, return the position of the number. Print an appropriate message if the number 
# is not present in the list.
def search_lst(lst):
    num=int(input("Enter a value to be searched : "))
    if num in lst:
        pos = lst.index(num)
        print("value num is present at",pos+1)
    else:    
        print("number is not present in the list")

# main program
lst=[1,2,3,4,5]
print(lst)

search_lst(lst)