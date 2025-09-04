# This code prints the string "hello world" in reverse order using a while loop.
# Define the string to be processed.
str = "hello world"

# Initialize a counter to start from the last index of the string.
i = 10

# Loop backwards from the end of the string to the beginning.
while i >= 0:
    # Print the character at the current index.
    print(str[i], end='')

    # Decrement the counter to move to the previous character.
    i = i - 1

# Print a new line after the loop has finished.
print(' ')
# The output of the above code will be: dlrow olleh

'''
str="hello world"
i=10
while i>=0:
    print(str[i],end='')
    i=i-1
print(' ')
'''