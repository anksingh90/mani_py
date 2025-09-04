#Write a program using user defined function that accepts an integer and increments the value by 5. Also display the id of argument (before function call), id of parameter before increment and after increment.
#Function to add 5 to a user input number
#The requirements are listed below:
	#1. Display the id()of argument before function call.
	#2. The function should have one parameter to accept the argument
	#3. Display the value and id() of the parameter.
	#4. Add 5 to the parameter
	#5. Display the new value and id()of the parameter to check
		 #whether the parameter is assigned a new memory location or #not.

def sum(num1):
   num2=num1+5
   print(id(num2))

num1=5
print(id(num1))
sum(num1)
