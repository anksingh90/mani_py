str=input('Enter a string : ')
str1=str[::-1]
flag = True
for i in range(len(str)-1):
    if str[i] != str1[i]:
        print('This is not a palindrome')
        flag = False
        break

if flag: # if flag == True:
    print('This is a palindrome')