def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    mul=a*b
    return mul
def divide(a,b):
    div=a/b
    return div


print("welcome to calculator")
while True:
    print("press1:Sum")
    print("press2:Subtract")
    print("press3:Multiply")
    print("press4:Divide")
    print("press0:Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        a=int(input("Enter a number"))
        b=int(input("Enter a number"))
        print(sum(a,b))
    elif ch==2:
        a=int(input("Enter a number"))
        b=int(input("Enter a number"))
        n=subtract(a,b)
        print(n)
    elif ch==3:
        a=int(input("Enter a number"))
        b=int(input("Enter a number"))
        l=multiply(a,b)
        print(l)
    elif ch==4:
        a=int(input("Enter a number"))
        b=int(input("Enter a number"))
        k=divide(a,b)
        print(k)
    elif ch == 0:
        break
    else:
        print('Invalid response !')

        
       

      



