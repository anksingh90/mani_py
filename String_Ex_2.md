# 🐍 Python String Exercises : String - Ex 2 🚀

> A comprehensive collection of string manipulation exercises to master Python string operations

---

## 📋 Table of Contents
- [Exercise 1: String Slicing Operations](#exercise-1-string-slicing-operations)
- [Exercise 2: String Methods](#exercise-2-string-methods)
- [Exercise 3: Text Analysis Program](#exercise-3-text-analysis-program)
- [Exercise 4: Title Case Converter](#exercise-4-title-case-converter)
- [Exercise 5: Character Deletion Function](#exercise-5-character-deletion-function)
- [Exercise 6: Digit Sum Calculator](#exercise-6-digit-sum-calculator)
- [Exercise 7: Space to Hyphen Replacer](#exercise-7-space-to-hyphen-replacer)

---

## 🔤 Exercise 1: String Slicing Operations

**Given String:**
```python
mySubject = "Computer Science"
```

### ❓ Questions
Determine the output of the following string operations:

| Operation | Code | Description |
|-----------|------|-------------|
| **i.** | `print(mySubject[0:len(mySubject)])` | Full string slice |
| **ii.** | `print(mySubject[-7:-1])` | Negative indexing slice |
| **iii.** | `print(mySubject[::2])` | Every 2nd character |
| **iv.** | `print(mySubject[len(mySubject)-1])` | Last character |
| **v.** | `print(2*mySubject)` | String repetition |
| **vi.** | `print(mySubject[::-2])` | Reverse with step 2 |
| **vii.** | `print(mySubject[:3] + mySubject[3:])` | String concatenation |
| **viii.** | `print(mySubject.swapcase())` | Case swapping |
| **ix.** | `print(mySubject.startswith('Comp'))` | Prefix check |
| **x.** | `print(mySubject.isalpha())` | Alphabetic check |

---

## 🏠 Exercise 2: String Methods

**Given String:**
```python
myAddress = "WZ-1,New Ganga Nagar,New Delhi"
```

### ❓ Questions
Determine the output of the following string operations:

| Operation | Code | Description |
|-----------|------|-------------|
| **i.** | `print(myAddress.lower())` | Convert to lowercase |
| **ii.** | `print(myAddress.upper())` | Convert to uppercase |
| **iii.** | `print(myAddress.count('New'))` | Count occurrences |
| **iv.** | `print(myAddress.find('New'))` | Find first occurrence |
| **v.** | `print(myAddress.rfind('New'))` | Find last occurrence |
| **vi.** | `print(myAddress.split(','))` | Split by comma |
| **vii.** | `print(myAddress.split(' '))` | Split by space |
| **viii.** | `print(myAddress.replace('New','Old'))` | Replace substring |
| **ix.** | `print(myAddress.partition(','))` | Partition by delimiter |
| **x.** | `print(myAddress.index('Agra'))` | Find index (with error) |

---

## 📊 Exercise 3: Text Analysis Program

### 🎯 Objective
Write a program to analyze text input from the user.

### 📋 Requirements
- Input multiple lines of text until Enter is pressed
- Count and display:
  - 📝 Total characters (including spaces)
  - 🔤 Total alphabets
  - 🔢 Total digits
  - ⭐ Total special symbols
  - 📄 Total words

### 💡 Assumptions
- Each word is separated by a single space

### 🔧 Implementation Hints
```python
# Use input() in a loop
# Use string methods: isalpha(), isdigit(), isspace()
# Use split() to count words
```

---

## 🏷️ Exercise 4: Title Case Converter

### 🎯 Objective
Create a user-defined function to convert strings to title case.

### 📋 Function Specification
- **Function Name:** `to_title_case()`
- **Parameter:** String with multiple words
- **Return:** Title case string
- **Definition:** First letter of each word capitalized

### 💭 Example
```python
Input:  "hello world python"
Output: "Hello World Python"
```

---

## ✂️ Exercise 5: Character Deletion Function

### 🎯 Objective
Create a function to remove all occurrences of a specific character.

### 📋 Function Specification
- **Function Name:** `deleteChar()`
- **Parameters:** 
  - `string`: Input string
  - `char`: Character to delete
- **Return:** New string without the specified character

### 💭 Example
```python
Input:  deleteChar("Hello World", "l")
Output: "Heo Word"
```

---

## 🧮 Exercise 6: Digit Sum Calculator

### 🎯 Objective
Create a function to sum all digits in a string.

### 📋 Function Specification
- **Input:** String containing digits and other characters
- **Output:** Sum of all numeric digits
- **Method:** Extract digits and calculate their sum

### 💭 Example
```python
Input:  "abc123def45"
Output: 15  # (1+2+3+4+5)
```

---

## 🔄 Exercise 7: Space to Hyphen Replacer

### 🎯 Objective
Create a function to replace spaces with hyphens in a sentence.

### 📋 Function Specification
- **Input:** Sentence with words separated by spaces
- **Output:** Modified sentence with hyphens instead of spaces
- **Assumption:** Each word is separated by a single space

### 💭 Example
```python
Input:  "Python is awesome"
Output: "Python-is-awesome"
```

---

## 🎨 Tips for Success

> 💡 **Pro Tips:**
> - Practice string indexing and slicing
> - Understand positive and negative indexing
> - Master built-in string methods
> - Handle edge cases and errors
> - Test your functions with various inputs

---

## 📚 Additional Resources

- [Python String Documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [String Methods Reference](https://docs.python.org/3/library/stdtypes.html#string-methods)

---

*Happy Coding! 🚀*