#''' ask user to input string 
#extract all digits from the string
#if there are digits 
    #sum the colllected digits 
    #print out'the originalstr,the digits,sum of the digits'
    #if there are no digits printm message 'aw no didits ad printthe original str')'''
str=input("Enter your string")
sum=0
lst = []
for i in str:
    if i.isdigit():
        i = int(i)
        lst.append(i)
        sum=sum+i
print(str)
print(lst)
print(sum)