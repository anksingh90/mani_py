i=0
str="hello world"
while i<=len(str)-1:
    if str[i] in 'aeiou':
        print('*',end='')
    else:
        print(str[i], end='')
    i = i + 1
print(' ')