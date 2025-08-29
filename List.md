Chapter : 8 | Lists
1.  What is a List ?
Data type.
It is an ordered sequence.
It is mutable.

A string which consists of only characters, a list can have elements of different data types, such as integer, float, string, tuple or even another list.

1.1 Creating a List
Lst = [ 100, 23.5, 'Hello']

1.2 Accessing Elements in a List
print(Lst[0])		# Output : 100
print(Lst[5])		# IndexError: list index out of range

1.3 Lists are Mutable
lst[2] = 'Black'		# Output : 100, 23.5, Black

2. List Operations
2.1  Concatenation
Lst1 = [ 100, 23.5, 'Hello']
Lst2 = [ 200, 123.5, 'Black']
print(Lst1 + Lst2)
2.2  Repetition
print(Lst1 * 2)		#  [100, 23.5, 'Hello', 100, 23.5, 'Hello']
2.3  Membership
2.3.1  In
list1 = ['Red','Green','Blue']
print('Green' in list1)		# Output : True
2.3.2  Not In
list1 = ['Red','Green','Blue']
print('Green' not in list1)		# Output : False
2.4  Slicing - It is a way to extract a subset of elements from the list.
list[start:stop:step]
2.4.1  Basic Slicing
my_list = [1, 2, 3, 4, 5]
print(my_list[1:3])  # Output: [2, 3]
2.4.2  Omitting Start or Stop
my_list = [1, 2, 3, 4, 5]
print(my_list[:3])  # Output: [1, 2, 3]
print(my_list[2:])  # Output: [3, 4, 5]
2.4.3  Using Step
my_list = [1, 2, 3, 4, 5]
print(my_list[::2])  # Output: [1, 3, 5]
print(my_list[::-1])  # Output: [5, 4, 3, 2, 1]
2.4.4  Negative Indexes
my_list = [1, 2, 3, 4, 5]
print(my_list[-4 :-2])		# Output : [2, 3]

3.  Traversing a List : Access each element of the list
3.1  List Traversal Using for Loop
list1 = ['Red','Green','Blue','Yellow','Black']
for item in list1:
    print(item)
3.2  List Traversal Using while Loop
list1 = ['Red','Green','Blue','Yellow','Black']
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

4.  List Methods and Built-in Functions
len()  |   list()  |  append()  |  extend()  |  insert()  |  count()  |  index()  |  remove()  |  pop()  |  reverse()  |  sort()  |  sorted()  |  min()  |  max()  |  sum()

5.  Nested Lists : a list appears as an element of another list
list1 = [1,2,'a','c',[6,7,8],4,9]
List1[4]					# Output : [6, 7, 8]
List1[4][1]					# Output : 7

6.  Copying Lists
Option 1
list1 = [1,2,3]
list2 = list1
print(list2)			# Output : [1, 2, 3]
Option 2
list2 = list1[:]
Option 3
Lst2 = list(lst1)




