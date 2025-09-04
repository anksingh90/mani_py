# Replace all the vowels in the string "hello world" with '*'
# using a while loop and print the modified string.

# Initialize a counter for the loop.
i = 0

# Define the string to be processed.
str = "hello world"

# Loop through each character of the string.
while i <= len(str) - 1:
    # Check if the current character is a vowel.
    if str[i] in 'aeiou':
        # If it's a vowel, print an asterisk.
        print('*', end='')
    else:
        # Otherwise, print the character as is.
        print(str[i], end='')

    # Move to the next character.
    i = i + 1

# Print a new line at the end.
print(' ')
# The output of the above code will be: h*ll* w*rld

'''
i=0
str="hello world"
while i<=len(str)-1:
    if str[i] in 'aeiou':
        print('*',end='')
    else:
        print(str[i], end='')
    i = i + 1
print(' ')
'''