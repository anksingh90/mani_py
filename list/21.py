#writea program to generate the sequence: negative5,10,
#.  upto n,where n is an integer input
# by the user

value = int(input('Enter the nth term : '))

for i in range(1,value+1):
    if i%2 == 0:
        print(i*5)
    else:
        print(i*-5)