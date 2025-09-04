# WAP to calculate canvas amount for tent (radius and height input)
# This program calculates the total canvas area needed for a tent with cylindrical base and conical top
# It also computes the total cost based on unit price

# Sub-functions for area calculations

def CSA_conical(r, l):
    """
    Calculate Curved Surface Area of conical part of tent
    Formula: π * r * l (where l is slant height)
    Args: r - radius of cone base, l - slant height of cone
    Returns: curved surface area of conical section
    """
    return 3.14 * r * l

def CSA_cylindrical(r, h):
    """
    Calculate Curved Surface Area of cylindrical part of tent
    Formula: 2 * π * r * h
    Args: r - radius of cylinder, h - height of cylinder
    Returns: curved surface area of cylindrical section
    """
    return 2 * 3.14 * r * h

def total_price(canvas_area):
    """
    Calculate total price of tent canvas including GST
    Args: canvas_area - total canvas area required
    Prints: total price without GST and with GST
    Note: GST calculation appears to have an error - it shows same price twice
    """
    # Get unit price per square unit from user
    unit_price = int(input("Enter the unit price of the tent"))
    
    # Calculate total price (base price without GST)
    total_price = unit_price * canvas_area
    
    # Display total price without GST
    print("total price of tent", int(total_price))
    
    # Display total price with GST (currently shows same price - bug in original code)
    # Should be: total_price * 1.18 for 18% GST
    print("total price (with gst of 0.18) of tent", int(total_price))


# Main Program - Tent Canvas Area and Price Calculator

# Get tent dimensions from user
r = int(input("Enter the radius "))                           # Radius of tent base
h = int(input("Enter the height of cylindrical part"))        # Height of cylindrical section
l = int(input("Enter the slant height of conical part"))      # Slant height of conical top

# Calculate total canvas area needed
# Total area = Conical surface area + Cylindrical surface area
Canvas_area = CSA_conical(r, l) + CSA_cylindrical(r, h)

# Calculate and display total price
total_price(Canvas_area)  # Pass canvas area to price calculation function

'''
#wap to calculate cable amount for tent (radius and height i/p)
# sub_function

def CSA_conical(r,l):
    return 3.14*r*l

def CSA_cylindrical(r,h):
    return 2*3.14*r*h

def total_price(canvas_area):
    unit_price=int(input("Enter the unit price of the tent"))
    total_price = unit_price*canvas_area
    print("total price of tent",int(total_price))
    print("total price (with gst of 0.18) of tent",int(total_price))




# main program

r=int(input("Enter the radius "))
h=int(input("Enter the height of cylindrical part"))
l=int(input("Enter the slant height of conical part"))

Canvas_area=CSA_conical(r,l) + CSA_cylindrical(r,h)

total_price(Canvas_area) # calculating price
'''