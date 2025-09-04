#Write a program to find the sum of 1+ 1/8 + 1/27......1/n3, where n is the number input by the user.
sum=0
n=int(input("Enter the cube of a number"))
for i in range(1,n+1):
    val=1/i**3
    sum=sum+val
print(sum)    

