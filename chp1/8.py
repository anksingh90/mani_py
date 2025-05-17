'''
Movie Ticket Pricing: A cinema has different ticket prices based on age.
18 Children (under 13) pay $8.
19 Teenagers (13 to 19 inclusive) pay $12.
20 Adults (20 to 60 inclusive) pay $15.
21 Seniors (over 60) pay $10. Write a program that asks the user for their age and
prints the corresponding movie ticket price.
'''
age=int(input("Enter your age"))
if age>=0 and age<13:
    print("pay 8")
elif age>=13 and age<=19:
    print("pay 12") 
elif age>=20 and age<=60:
    print("pay 15") 
else:
    print("pay 10")    









