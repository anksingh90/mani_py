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




