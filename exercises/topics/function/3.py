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

