# perform delete function 
# delete from 3rd pos,deleteupto 5th pos,delete even values

lst=[2,6,5,3,4,9,8]
lst.pop(3)
print('Delete from 3 index value : ',lst)

lst=[2,6,5,3,4,9,8]
lst.pop(5)
print('Delete upto 5 index value : ',lst)

lst=[2,6,5,3,4,9,8]
del lst[::2]
print('Deleting even position value : ',lst)

lst=[2,6,5,3,4,9,8]
for i,values in enumerate(lst):
    if i%2 != 0:
        lst.pop(values)
print('Deleting even position value : ',lst)