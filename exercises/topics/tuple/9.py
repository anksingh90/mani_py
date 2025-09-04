#wap to compute the area and circumference of circle uing functions.
def area_circum(radius):
    area=3.14*radius**2
    circum=2*3.14*radius
    print(area)
    print(circum)

r=int(input("Enter a radius"))
area_circum(r)