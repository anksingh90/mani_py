#Q4 : Write a program to input n numbers from the user. Store these numbers in a tuple. Print the maximum and minimum
#number from this tuple. 
#Program to input n numbers from the user. Store these numbers
#in a tuple. Print the maximum and minimum number from this tuple.
lst=[]
len=int(input("Enter a length of list"))
for i in range(1,len):
    num1=input("Enter an number")
    lst.append(num1)

tup=tuple(lst)
print(min(lst))
print(max(lst)) 