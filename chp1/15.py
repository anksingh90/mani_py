#calculate BMI
weight=float(input("Enter your weight in kg : "))
height=float(input("Enter your height in feet : "))
height_n=height*0.3048
BMI=weight/(height_n*height_n)
print(BMI)
