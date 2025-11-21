# write a menu driven program to input your friends name, no. 
#perform these instructions
#display name,phone of all
# add new name ,no. in dict
#modify phone no. of friend
#delete entry 
#search details
#display the dict in sort in order of name
stu={}
while True:
    print('press 1 to display name and phone number of all friends')
    print('press 2 to add new name and number in dictonary')
    print('press 3 to modify phone number of friend')
    print('press 4 to delete entry')
    print('press 5 to search details ')
    print('press 6 to display the dictionary in sort in order of name')
    ch=int(input("Enter your choice"))
    if ch==1:
        length=int(input('Enter number of entries'))
        for i in range(length):
            name=input('Enter name of friends')
            Phone_number=int(input("Enter phone number of friends"))
            stu[name]=[Phone_number]
            print(stu)
    elif ch==2: