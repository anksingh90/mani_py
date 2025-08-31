# Lists in Python (Chapter 8)

## 1. What is a List?
- A fundamental data type in Python
- An ordered sequence of elements
- Mutable (can be modified after creation)
- Can contain elements of different data types (integer, float, string, tuple, or even another list)

### 1.1 Creating a List
```python
Lst = [100, 23.5, 'Hello']
```

### 1.2 Accessing Elements
```python
print(Lst[0])     # Output: 100
print(Lst[5])     # IndexError: list index out of range
```

### 1.3 Mutability
```python
lst[2] = 'Black'  # Changes third element to 'Black'
```

## 2. List Operations

### 2.1 Concatenation
```python
Lst1 = [100, 23.5, 'Hello']
Lst2 = [200, 123.5, 'Black']
print(Lst1 + Lst2)  # Combines both lists
```

### 2.2 Repetition
```python
print(Lst1 * 2)   # Output: [100, 23.5, 'Hello', 100, 23.5, 'Hello']
```

### 2.3 Membership Operations
#### Using 'in'
```python
list1 = ['Red', 'Green', 'Blue']
print('Green' in list1)      # Output: True
```

#### Using 'not in'
```python
print('Green' not in list1)  # Output: False
```

### 2.4 Slicing Operations
Syntax: `list[start:stop:step]`

#### 2.4.1 Basic Slicing
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[1:3])    # Output: [2, 3]
```

#### 2.4.2 Omitting Start/Stop
```python
print(my_list[:3])     # Output: [1, 2, 3]
print(my_list[2:])     # Output: [3, 4, 5]
```

#### 2.4.3 Using Step
```python
print(my_list[::2])    # Output: [1, 3, 5]
print(my_list[::-1])   # Output: [5, 4, 3, 2, 1]
```

#### 2.4.4 Negative Indexing
```python
print(my_list[-4:-2])  # Output: [2, 3]
```

## 3. List Traversal

### 3.1 Using for Loop
```python
list1 = ['Red', 'Green', 'Blue', 'Yellow', 'Black']
for item in list1:
    print(item)
```

### 3.2 Using while Loop
```python
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
```

## 4. List Methods and Built-in Functions
- `len()` - Get length
- `list()` - Create list
- `append()` - Add element
- `extend()` - Add multiple elements
- `insert()` - Insert at position
- `count()` - Count occurrences
- `index()` - Find index
- `remove()` - Remove element
- `pop()` - Remove and return
- `reverse()` - Reverse list
- `sort()` - Sort in-place
- `sorted()` - Return sorted list
- `min()` - Minimum value
- `max()` - Maximum value
- `sum()` - Sum of elements

## 5. Nested Lists
```python
list1 = [1, 2, 'a', 'c', [6, 7, 8], 4, 9]
print(list1[4])      # Output: [6, 7, 8]
print(list1[4][1])   # Output: 7
```

## 6. Copying Lists
### Method 1: Direct Assignment
```python
list1 = [1, 2, 3]
list2 = list1
```

### Method 2: Slice Copy
```python
list2 = list1[:]
```

### Method 3: List Constructor
```python
list2 = list(list1)
```

## 7. Practice Questions

### Question 1: Menu Driven List Operations
Write a menu driven program to perform various list operations, such as:
- Append an element
- Insert an element
- Append a list to the given list
- Modify an existing element
- Delete an existing element from its position
- Delete an existing element with a given value
- Sort the list in ascending order
- Sort the list in descending order
- Display the list

### Question 2: Calculate Average Marks
Write a program to calculate average marks of n students using a function where n is entered by the user.

### Question 3: Search Element in List
Write a user-defined function to check if a number is present in the list or not. If the number is present, return the position of the number. Print an appropriate message if the number is not present in the list.

### Question 4: Student Record Operations
The record of a student (Name, Roll No., Marks in five subjects and percentage of marks) is stored in the following list:
```python
stRecord = ['Raman', 'A-36', 56, 98, 99, 72, 69, 78.8]
```
Write Python statements to retrieve the following information from the list stRecord:

a) Percentage of the student

b) Marks in the fifth subject

c) Maximum marks of the student

d) Roll no. of the student

e) Change the name of the student from 'Raman' to 'Raghav'

### Question 5: Find Median
Write a program to read a list of n integers and find their median.

### Question 6: Remove Duplicates
Write a program to read a list of elements. Modify this list so that it does not contain any duplicate elements, i.e., all elements occurring multiple times in the list should appear only once.

### Question 7: Count Number Occurrences
Write a Python script to input a number and count the occurrences of that number in a given list.
```python
list1 = [10, 20, 30, 40, 10, 50, 10]
```

### Question 8: Split Temperature List
The temperature of a week is given in WTemp list in the form of days and their temperature values:
```python
WTemp = ['Mon', 45, 'Tue', 43, 'Wed', 42, 'Thu', 40, 'Fri', 38, 'Sat', 40, 'Sun', 38]
```
Write a program to create and print two separate lists as given below:
```python
Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
Degrees = [45, 43, 42, 40, 38, 40, 38]
```

### Question 9: Unique and Duplicate Items
Write a program to display unique and duplicate items of a given list into two different lists.
```python
Input: L1 = [2, 7, 1, 4, 9, 5, 1, 4, 3]
Output: 
Unique items: [2, 7, 1, 4, 9, 5, 3]
Duplicate items: [1, 4]
```

### Question 10: Exchange List Halves
Write a program to exchange first-half elements of list with second-half elements assuming list is having even number of elements.

### Question 11: Filter Strings Starting with 'A'
Write a program in Python to display those strings which are starting with character 'A' or 'a' from the given list L.
```python
L = ["RINKU", "AUSHIM", "VIJAYA", "AKHTAR", "LEENA", "TARUN", "AMAR"]
```

### Question 12: Advanced List Operations
Write a menu-driven program to do the various list operations:
- Sort list in ascending order using bubble sort
- Sort list in descending order using Insertion sort
- Search an element
- Count an element
- Display list

### Question 13: Banking System
Create a menu-driven banking system program with the following operations:
- Open a savings bank account
- Add a customer
- Deposit money
- Display sorted records
- Close/delete account

The program should:
1. Accept choices for Deposit and Withdrawal
2. Accept transaction amount
3. Perform the transaction
4. Display the balance




