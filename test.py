# Write a program to check if a string is a palindrome or not. (A string is called palindrome if it reads same 
# backwards as forward. For example, Kanak is a palindrome.
i=0
str="hello world"  
ch="l"
while i<=len(str)-1:
    if str[i]==ch:
        i=i+1
        continue
    else:
        print(str[i],end='')
    i=i+1
print('')        

    
