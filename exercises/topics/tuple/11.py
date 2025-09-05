#Write a program to read email IDs of n number of students and store them in a tuple. Create two new
#tuples, one to store only the usernames from the email IDs and second to store domain names from
# the email IDs. Print all three tuples at the end of the program. [Hint: You may use the function split()]

tup_name=()
tup_email=()
n=int(input("Enter the number of students "))
for i in range(1,n+1):
    email = input('Enter your email address : ')
    stu_name, stu_email = email.split('@')
    tup_name=tup_name + (stu_name,)
    tup_email=tup_email + (stu_email,)

print(tup_name)
print(tup_email)