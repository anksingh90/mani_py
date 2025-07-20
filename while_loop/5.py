'''
Write a program to check if a string is a palindrome or not. (A string is called palindrome if it reads same 
backwards as forward. For example, Kanak is a palindrome.)
'''

i=0
str="kanak"
str1=str[::-1]
if str==str1:
    print("palindrome")
else:
    print("not a palindrome")    
