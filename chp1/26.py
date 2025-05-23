n = int(input('Enter a number for permutation : '))
per = 1
for i in range(1,n+1):
    per = per * i
print('Permutation of : ', n,'is : ',per)