# Order Discount Calculator
# Ask user for order value and apply discount based on amount:
# - If order value is over 500 rupees: give 20% discount
# - If order value is 500 rupees or less: give 5% discount

# Get order value from user
# Note: Comment mentions "string/char" but input is converted to integer
a = int(input("Enter the order value : "))  # Convert string input to integer

# Check order value and apply appropriate discount
if a > 500:
    # For orders greater than 500 rupees - apply 20% discount
    print("discount of 20% ")
elif a <= 500:
    # For orders of 500 rupees or less - apply 5% discount
    print("discount of 5% ")


'''
#ask user for order value if order value is over 500 ruppees give 20/ discount and if less than 500 rupees 5/discount.
a=int(input("Enter the order value : ")) # string/char

if a>500:
    print("discount of 20% ")
elif a<=500:
    print ("discount of 5% ")
'''