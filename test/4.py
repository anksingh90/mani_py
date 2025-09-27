#fabonacci series
#In for loop
A=0
N=1
n=10
for i in range(0,n+1):
    print(A,end='')
    A,N=N,A+N

#In while loop
A=0
N=1
i=1
n=10
while i<=n :
    print(A,end='')
    i=i+1
    A,N=N,A+N
    