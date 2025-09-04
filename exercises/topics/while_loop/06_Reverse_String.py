# Prompt the user to enter a string and store it.
str = input('Enter a string : ')

# Create a reversed version of the string using slicing.
str1 = str[::-1]

# Initialize a boolean flag to true, assuming the string is a palindrome.
flag = True

# Loop through the string to compare characters.
for i in range(len(str)):
    # If a character does not match its corresponding character in the reversed string...
    if str[i] != str1[i]:
        # ...print that it's not a palindrome.
        print('This is not a palindrome')
        # Set the flag to false.
        flag = False
        # Exit the loop as we've found a mismatch.
        break

# If the flag is still true after the loop, the string is a palindrome.
if flag:
    print('This is a palindrome')


'''
str=input('Enter a string : ')
str1=str[::-1]
flag = True
for i in range(len(str)-1):
    if str[i] != str1[i]:
        print('This is not a palindrome')
        flag = False
        break

if flag: # if flag == True:
    print('This is a palindrome')
'''