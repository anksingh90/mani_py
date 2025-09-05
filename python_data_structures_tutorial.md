# 🎯 Python Data Structures – Essential Guide for Class XI

## 📚 Table of Contents
1. [Tuples](#-1-tuples)
2. [Dictionaries](#-2-dictionaries)
3. [Quick Comparison](#-3-quick-reference)

---

## 🔹 1. Tuples
### 📦 What is a Tuple?
> *"Tuples are immutable sequences, typically used to store collections of heterogeneous data"*

- An **ordered collection** of elements 🔢
- **Immutable** → rock-solid, unchangeable! 🔒
- Defined using **round brackets `()`** 

### ✨ Creating Tuples
```python
empty = ()                 # Empty tuple
single = (3,)             # Single element (comma is important!)
nums = (1, 2, 3)          # Number tuple
mixed = (1, 2.5, 'a')     # Mixed data types
```

### 🛠 Tuple Functions
| Function | Description | Example |
|----------|-------------|---------|
| `len(t)` | Get length | `len((1,2,3)) → 3` |
| `max(t)` | Maximum value | `max((1,5,3)) → 5` |
| `min(t)` | Minimum value | `min((1,5,3)) → 1` |
| `index(x)` | Find position | `(1,2,3).index(2) → 1` |
| `count(x)` | Count occurrences | `(1,2,2).count(2) → 2` |

### 🎮 Tuple Operations
```python
# 🔄 Traversing
colors = ('red', 'green', 'blue')
for color in colors:
    print(f"Color: {color}")

# 🔗 Joining
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)    # (1, 2, 3, 4)

# 📝 Slicing
week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
print(week[1:4])  # ('Tue', 'Wed', 'Thu')
```

---

## 🔹 2. Dictionaries
### 📖 What is a Dictionary?
> *"Dictionaries are Python's implementation of a key-value store"*

- Collection of **key–value pairs** 🔑➡️📦
- **Mutable** and **unordered** 
- Defined using **curly braces `{}`**

### 🌟 Dictionary Example
```python
student = {
    'name': 'Alex',
    'age': 16,
    'grades': {'math': 95, 'science': 98},
    'active': True
}
```

### ⚡ Dictionary Methods
| Method | Purpose | Example |
|--------|---------|---------|
| `get(key)` | Safe value access | `dict.get('key', default)` |
| `keys()` | Get all keys | `dict.keys()` |
| `values()` | Get all values | `dict.values()` |
| `items()` | Get key-value pairs | `dict.items()` |
| `update()` | Merge dictionaries | `dict1.update(dict2)` |

### 🎯 Common Operations
```python
# 🔍 Accessing Values
print(student['name'])      # Direct access
print(student.get('age'))   # Safe access

# ➕ Adding/Updating
student['class'] = 'XI-A'   # Add new
student['age'] = 17         # Update

# ❌ Removing
del student['active']       # Remove key
student.pop('grades')       # Remove and return

# 🔄 Iteration
for key, value in student.items():
    print(f"{key}: {value}")
```

---

## 🔹 3. Quick Reference
### 📊 Data Structure Comparison

| Feature | Tuple | Dictionary |
|---------|-------|------------|
| **Symbol** | `()` | `{}` |
| **Mutability** | 🔒 Immutable | ✏️ Mutable |
| **Ordering** | ✅ Ordered | ❌ Unordered |
| **Access** | Index-based | Key-based |
| **Best For** | Fixed data collections | Key-value mappings |
| **Performance** | Fast access | Fast lookups |

> 💡 **Pro Tip**: Choose tuples for immutable sequences and dictionaries when you need key-based lookups!

---

*Happy Coding! 🚀*
