s1=int(input("Enter value of side1 : "))
s2=int(input("Enter value of side2 : "))
s3=int(input("Enter value of side3 : "))
if s1==s2 and s2==s3 and s1==s3:
    print("Equilateral triangle")
elif s1==s2 or s1==s3:
    print("Isosceles triangle") 
elif s1!=s2 and s2!=s3 and s1!=s3:
    print("Scalene triangle") 

