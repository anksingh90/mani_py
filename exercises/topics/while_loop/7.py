def add():
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    add=a+b
    print("the sum of", a, "&", b ,"is",add)


while True:
    ch=int(input("Enter your choice"))
    if ch==1:
        print("press1=sum")
        add()
    elif ch==2:
        print("press2=sub")  
        print("sub")
    elif ch==3:
        print("press3=exit")  
        break
    else:
        print("invalid input")    

