# Practice Programming Exercises : List - Ex 2 🚀

## 1. Maximum of Two Numbers
Find maximum of two numbers in Python using:
- `max()` function
- `if-else` statement

## 2. List Length Calculator
Calculate the length of a list in Python using:
- Loop implementation
```python
# Example:
my_list = [1, 2, 3, 4, 5]
count = 0
for _ in my_list:
    count += 1
print(f"Length: {count}")
```

## 3. Minimum Number Finder
Find minimum of two numbers using:
- Conditional statements
```python
# Example:
def find_min(a, b):
    return a if a < b else b
```

## 4. Element Interchange 🔄
Write a program to interchange first and last elements in a list.

## 5. Element Counter
Count occurrences of an element in a list using:
- `count()` method
- Loop implementation
```python
# Example using count()
numbers = [1, 2, 2, 3, 2, 4, 5]
count = numbers.count(2)  # Returns 3
```

## 6. List Multiplier ✖️
Multiply all numbers in the list using:
- Loop implementation
```python
# Example:
result = 1
for num in numbers:
    result *= num
```

## 7. Second Largest Number
Find second largest number using:
- Loop implementation
- `sort()` method
```python
# Using sort()
numbers.sort()
second_largest = numbers[-2]
```

## 8. Even/Odd Separator
Print even and odd numbers from a list:
```python
# Example output:
Even numbers: [2, 4, 6, 8]
Odd numbers: [1, 3, 5, 7]
```

## 9. Number Sign Counter ➕➖
Count positive and negative numbers in a list:
```python
# Example output:
Positive numbers: 5
Negative numbers: 3
```

## 10. Multiple Elements Remover
Remove multiple elements from a list in Python.

## 11. List Prepender
Append elements at the beginning of list using:
- `insert()` method
```python
# Example:
my_list.insert(0, new_element)
```

## 12. List Comparison
Check if two lists are identical using:
- Loop implementation
- Equality operator (`==`)
```python
# Using equality operator
list1 = [1, 2, 3]
list2 = [1, 2, 3]
are_identical = (list1 == list2)  # Returns True
```

## 💡 Tips
- Use appropriate error handling
- Validate inputs
- Consider edge cases
- Test with different scenarios

## Example Output Format
```python
Input: [1, 2, 3, 4, 5]
Processing...
Result: Operation completed!
```