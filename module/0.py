# help function - Module

# importing module from file

import math

print('***** Area of Circle *******')
radius = int(input('Enter the radius for circle : '))
area = math.pi * radius * radius # calling pi functions from math module
print('Area of circle : ', area) 


# printing Trigonometric Functions values
print('\n***** Trigonometric Functions values *******')
angle = int(input('Enter the angle to find the Trigonometric Functions values : '))
print(math.cos(angle))
print(math.sin(angle))
print(math.tan(angle))

# math.pow
print('\n***** math.pow *******')
value = int(input('Enter the value  : '))
power = int(input('Enter the power : '))
print(math.pow(value,power))

# Other functions

print('Math Square Root of 25 : ',math.sqrt(25))
print('Factorial of 5 : ',math.factorial(value))

# from math import factorial : importing sub-fuction of module