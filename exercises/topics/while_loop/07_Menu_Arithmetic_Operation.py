# This function takes two numbers from the user and prints their sum.
def add():
    # Get the first number from the user.
    a = int(input("Enter a number: "))
    # Get the second number from the user.
    b = int(input("Enter a number: "))
    # Calculate the sum.
    sum_result = a + b
    # Print the result.
    print("The sum of", a, "&", b, "is", sum_result)

# This function takes two numbers from the user and prints their difference.
def subtract():
    # Get the first number.
    a = int(input("Enter a number: "))
    # Get the second number.
    b = int(input("Enter a number: "))
    # Calculate the difference.
    diff_result = a - b
    # Print the result.
    print("The difference of", a, "&", b, "is", diff_result)

# Start an infinite loop to display the calculator menu.
while True:
    # Display the menu options.
    print("Press 1 for Sum")
    print("Press 2 for Subtract")
    print("Press 3 to Exit")
    
    # Get the user's choice.
    ch = int(input("Enter your choice: "))
    
    # Perform an action based on the user's choice.
    if ch == 1:
        # Call the add() function for addition.
        add()
    elif ch == 2:
        # Call the subtract() function for subtraction.
        subtract()
    elif ch == 3:
        # Exit the program loop.
        print("Exiting the calculator. Goodbye!")
        break
    else:
        # Handle invalid input.
        print("Invalid input")


'''
def add():
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    add=a+b
    print("the sum of", a, "&", b ,"is",add)

    while True:
    ch=int(input("Enter your choice"))
    if ch==1:
        print("press1=sum")
        add()
    elif ch==2:
        print("press2=sub")  
        print("sub")
    elif ch==3:
        print("press3=exit")  
        break
    else:
        print("invalid input")
'''