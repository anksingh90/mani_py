lst_length=int(input("Enter length of the list"))
lst=[]
for i in range(lst_length):
    a=int(input("Enter the value for list"))
    lst.append(a)

print('Listed created : ',lst)

pos = int(input('Enter position to edit value : '))
p_value = int(input('Enter value to be updated : '))

lst[pos-1]=p_value
print('Updated Listed : ',lst)