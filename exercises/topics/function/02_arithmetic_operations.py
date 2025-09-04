# Simple Calculator Program
# This program provides basic arithmetic operations through a menu-driven interface

# Function to add two numbers
def sum(a, b):
    """
    Add two numbers and return the result
    Args: a, b - numeric values to be added
    Returns: sum of a and b
    """
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    """
    Subtract second number from first number
    Args: a, b - numeric values (a - b)
    Returns: difference of a and b
    """
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    """
    Multiply two numbers and return the result
    Args: a, b - numeric values to be multiplied
    Returns: product of a and b
    """
    # Store multiplication result in variable before returning
    mul = a * b
    return mul

# Function to divide two numbers
def divide(a, b):
    """
    Divide first number by second number
    Args: a, b - numeric values (a / b)
    Returns: quotient of a divided by b
    Note: No zero division check implemented
    """
    # Store division result in variable before returning
    div = a / b
    return div


# Main Program - Calculator Interface
print("welcome to calculator")

# Infinite loop for continuous calculator operation
while True:
    # Display menu options to user
    print("press1:Sum")
    print("press2:Subtract")
    print("press3:Multiply")
    print("press4:Divide")
    print("press0:Exit")
    
    # Get user's choice for operation
    ch = int(input("Enter your choice"))
    
    # Addition operation
    if ch == 1:
        # Get two numbers from user
        a = int(input("Enter a number"))
        b = int(input("Enter a number"))
        # Call sum function and print result directly
        print(sum(a, b))
    
    # Subtraction operation
    elif ch == 2:
        # Get two numbers from user
        a = int(input("Enter a number"))
        b = int(input("Enter a number"))
        # Call subtract function, store result in variable n, then print
        n = subtract(a, b)
        print(n)
    
    # Multiplication operation
    elif ch == 3:
        # Get two numbers from user
        a = int(input("Enter a number"))
        b = int(input("Enter a number"))
        # Call multiply function, store result in variable l, then print
        l = multiply(a, b)
        print(l)
    
    # Division operation
    elif ch == 4:
        # Get two numbers from user
        a = int(input("Enter a number"))
        b = int(input("Enter a number"))
        # Call divide function, store result in variable k, then print
        k = divide(a, b)
        print(k)
    
    # Exit option
    elif ch == 0:
        # Break out of the while loop to end program
        break
    
    # Handle invalid menu choices
    else:
        print('Invalid response !')
        # Loop continues, showing menu again

'''
def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    mul=a*b
    return mul
def divide(a,b):
    div=a/b
    return div

print("welcome to calculator")
while True:
    print("press1:Sum")
    print("press2:Subtract")
    print("press3:Multiply")
    print("press4:Divide")
    print("press0:Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        a=int(input("Enter a number"))
        b=int(input("Enter a number"))
        print(sum(a,b))
    elif ch==2:
        a=int(input("Enter a number"))
        b=int(input("Enter a number"))
        n=subtract(a,b)
        print(n)
    elif ch==3:
        a=int(input("Enter a number"))
        b=int(input("Enter a number"))
        l=multiply(a,b)
        print(l)
    elif ch==4:
        a=int(input("Enter a number"))
        b=int(input("Enter a number"))
        k=divide(a,b)
        print(k)
    elif ch == 0:
        break
    else:
        print('Invalid response !')
'''