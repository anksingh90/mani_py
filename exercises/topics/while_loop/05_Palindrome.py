# Initialize a counter. (This line is not actually used in the new code, but I'll keep it for context)
i = 0

# Define the string to check.
str = "kanak"

# Create a reversed version of the string using slicing.
str1 = str[::-1]

# Check if the original string is the same as the reversed string.
if str == str1:
    # If they are the same, print that the string is a palindrome.
    print("palindrome")
else:
    # Otherwise, print that the string is not a palindrome.
    print("not a palindrome")


'''
Write a program to check if a string is a palindrome or not. (A string is called palindrome if it reads same 
backwards as forward. For example, Kanak is a palindrome.)

i=0
str="kanak"
str1=str[::-1]
if str==str1:
    print("palindrome")
else:
    print("not a palindrome")
'''
