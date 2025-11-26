# calculate area of circle,circumference of circle,area of rectangle
import math 
print("area of circle")
radius=int(input("Enter radius of a circle"))
area=math.pi*radius*radius
circumference= 2*math.pi*radius
print("Area of a circle",area)
print("Circumference of a circle",circumference)

print("area of rectangle")
length=int(input("Enter length"))
breath=int(input("Enter breath"))
print("area of a rectangle",2*length*breath)