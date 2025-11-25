#write a menu driven program to input your friends name, no. 
#perform these instructions
#display name,phone of all
#add new name ,no. in dict
#modify phone no. of friend
#delete entry 
#search details
#display the dict in sort in order of name
stu={'Amit':1234567,'Roy':2323232,'Mani':1234543}
while True:
    print('press 1 to display name and phone number of all friends')
    print('press 2 to add new name and number in dictonary')
    print('press 3 to modify phone number of friend')
    print('press 4 to delete entry')
    print('press 5 to search details ')
    print('press 6 to display the dictionary in sort in order of name')
    ch=int(input("Enter your choice : "))
    if ch==1:
        print('Name \t Telephone_Number')
        for keys, values in stu.items():
            print(keys,'\t', values)
    elif ch==2:
        length=int(input("Enter the number of entries to be added"))
        for i in range(length):
            name=input("Enter new name to be added in dictonary")
            Phone_number=int(input("Enter phone number in dictonary"))
            stu[name]=[Phone_number]
        print(stu)
    elif ch==3:
        name=input("Enter name to be searched : ")
        if name in stu: # membership operator
            Phone_number=int(input("Enter Phone_number : "))
            stu[name]=[Phone_number]
            print(stu)
        else:
            print("invalid input")
    elif ch==4:
        name=input("Enter name")
        if name in stu:
            stu.pop(name)
            print(stu)
        else:
            print("invalid input")    
    elif ch==5:
        name=input("Enter name")
        if name in stu:
            print('Name found in dictionary !')
        else:
            print("invalid input") 
    elif ch==6:
        sorted_stu = dict(sorted(stu.items()))
        print(sorted_stu)