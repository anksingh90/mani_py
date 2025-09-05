# 🐍 Python Data Structures – Lists, Tuples, and Dictionaries (Class XI Tutorial)

## 🔹 1. Lists
### What is a List?
- A **list** is a sequence of values of any type.  
- Lists are **mutable** → elements can be changed after creation.  
- Defined using **square brackets `[]`**.

**Examples:**
```python
empty = []
numbers = [1, 2, 3]
mixed = ['a', 1, 'b', 2]
```

### Indexing in Lists
- Lists support **two-way indexing**:  
  - Positive indexing starts from `0`.  
  - Negative indexing starts from `-1` (last element).  

```
List = ['P','Y','T','H','O','N']
Index =  0   1   2   3   4   5
Index = -6  -5  -4  -3  -2  -1
```

### List Operators
- **Joining (`+`)**
```python
l1 = [1, 2, 3]
l2 = [4, 5]
print(l1 + l2)   # [1, 2, 3, 4, 5]
```

- **Replication (`*`)**
```python
l1 = [1, 2]
print(l1 * 2)   # [1, 2, 1, 2]
```

- **Membership (`in`, `not in`)**
```python
my_list = [10, 20, 30]
print(20 in my_list)      # True
print(40 not in my_list)  # True
```

- **Comparison** → All relational operators work (`>`, `<`, `==`, etc.).

### List Slicing
```python
nums = [10, 12, 14, 20, 22, 24, 30]
print(nums[2:5])   # [14, 20, 22]
print(nums[-4:-1]) # [20, 22, 24]
```

### List Functions / Methods
| Method | Use |
|--------|-----|
| `append(x)` | Add single item |
| `extend([..])` | Add multiple items |
| `insert(pos, x)` | Insert at position |
| `index(x)` | Find first occurrence |
| `pop(i)` | Remove by index |
| `remove(x)` | Remove first matching item |
| `clear()` | Remove all items |
| `count(x)` | Count occurrences |
| `reverse()` | Reverse list |
| `sort()` | Sort ascending |

**Examples:**
```python
l = [1, 3, 2]
l.append(4)          # [1, 3, 2, 4]
l.sort()             # [1, 2, 3, 4]
l.remove(2)          # [1, 3, 4]
```

### List Manipulation
- **Update:**
```python
l = [1, 2, 3]
l[2] = 4   # [1, 2, 4]
```

- **Delete:**
```python
l = [10, 12, 13, 14]
del l[2]   # [10, 12, 14]
```

---

## 🔹 2. Tuples
### What is a Tuple?
- An **ordered collection** of elements.  
- **Immutable** → cannot change elements once created.  
- Defined using **round brackets `()`**.

**Examples:**
```python
empty = ()
single = (3,)           # single element tuple (comma required)
nums = (1, 2, 3)
mixed = (1, 2.5, 'a')
```

### Tuple Functions
| Function | Use |
|----------|-----|
| `len(t)` | Length |
| `max(t)` | Maximum value |
| `min(t)` | Minimum value |
| `index(x)` | Index of element |
| `count(x)` | Count occurrences |
| `tuple(seq)` | Convert sequence to tuple |

**Examples:**
```python
t = (10, 5, 78)
print(len(t))     # 3
print(max(t))     # 78
print(min(t))     # 5
```

### Tuple Operations
- **Traversing**
```python
t = ('p', 'y', 't', 'h', 'o', 'n')
for ch in t:
    print(ch)
```

- **Joining**
```python
t1 = (1, 2, 3)
t2 = (4, 5)
print(t1 + t2)   # (1, 2, 3, 4, 5)
```

- **Replication**
```python
t1 = (1, 2)
print(t1 * 2)    # (1, 2, 1, 2)
```

- **Slicing**
```python
t = (10, 12, 14, 20, 22, 24, 30)
print(t[2:5])    # (14, 20, 22)
```

---

## 🔹 3. Dictionaries
### What is a Dictionary?
- A collection of **key–value pairs**.  
- **Mutable** and **unordered**.  
- Defined using **curly braces `{}`**.  

**Example:**
```python
emp = {'name': 'John', 'age': 24, 'salary': 10000}
```

### Dictionary Functions / Methods
| Method | Use |
|--------|-----|
| `len(d)` | Number of key-value pairs |
| `clear()` | Remove all items |
| `get(key)` | Get value safely |
| `keys()` | List of keys |
| `values()` | List of values |
| `items()` | List of (key, value) pairs |
| `update(d2)` | Merge dictionaries |

**Examples:**
```python
emp = {'name': 'John', 'age': 24, 'salary': 10000}

print(emp.keys())      # ['name','age','salary']
print(emp.get('age'))  # 24

emp['dept'] = 'Sales'  # add new key
emp.pop('age')         # remove a key
```

### Dictionary Operations
- **Traversing**
```python
for key in emp:
    print(key, emp[key])
```

- **Adding Elements**
```python
emp['dept'] = 'Sales'
```

- **Deleting Elements**
```python
del emp['salary']
```

- **Checking Key Existence**
```python
print('age' in emp)       # True
print('bonus' not in emp) # True
```

---

## 🔹 4. Quick Reference – Comparison of Data Structures

| Feature      | List | Tuple | Dictionary |
|--------------|------|-------|------------|
| **Mutable**  | ✅   | ❌    | ✅ |
| **Ordered**  | ✅   | ✅    | ❌ |
| **Indexed**  | Numeric | Numeric | Key-based |
| **Duplicates** | Allowed | Allowed | Keys ❌, Values ✅ |
