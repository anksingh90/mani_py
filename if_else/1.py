#ask user for order value if order value is over 500 ruppees give 20/ discount and if less than 500 rupees 5/discount.

a=int(input("Enter the order value : ")) # string/char

if a>500:
    print("discount of 20% ")
elif a<=500:
    print ("discount of 5% ")
