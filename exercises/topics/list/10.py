# Write a program using a user defined function calcFact() to calculate and display the factorial of a number num passed as an argument.
#Function to calculate factorial
#The requirements are listed below:
	#1. The function should accept one integer argument from user.
	#2. Calculate factorial. For example:
	#3. Display factorial

def calcfact(num1):
    fact=1
    i=1
    while i<=num1:
        fact=fact*i
        i=i+1
    print(fact)

num1=int(input("Enter a number"))

calcfact(num1)
