#Write a program to find and print the grade of a student when the user inputs their percentage. 
# Grades are allocated as given in the table below:

marks=int(input("Enter your percentage"))
if marks>90:
    print("Grade A")
elif 80<marks<90:
    print("Grade B") 
elif  70<marks<80:
    print("Grade C")    
elif 60<marks<70:
    print("Grade D")     
elif marks<60:
    print("Grade E")
