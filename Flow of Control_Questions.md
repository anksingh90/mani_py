# NCERT Question Bank - Flow of Control

## Basic Concepts
1. **Difference between `else` and `elif`**
   - What is the difference between `else` and `elif` construct of if statement?

2. **`range()` Function**
   - What is the purpose of `range()` function? 
   - Give one example.

3. **Control Statements**
   - Differentiate between `break` and `continue` statements using examples.

4. **Loop Concepts**
   - What is an infinite loop?
   - Give one example.

## 5. Program Output Questions
### Find the output of the following code segments:

```python
# (i)
a = 110
while a > 100:
    print(a)
    a -= 2
```

```python
# (ii)
for i in range(20,30,2):
    print(i)
```

```python
# (iii)
country = 'INDIA'
for i in country:
    print(i)
```

```python
# (iv)
i = 0; sum = 0
while i < 9:
    if i % 4 == 0:
        sum = sum + i
    i = i + 2
print(sum)
```

```python
# (v)
for x in range(1,4):
    for y in range(2,5):
        if x * y > 10:
            break
        print(x * y)
```

```python
# (vi)
var = 7
while var > 0:
    print('Current variable value: ', var)
    var = var - 1
    if var == 3:
        break
    else:
        if var == 6:
            var = var - 1
            continue
    print("Good bye!")
```

## Programming Exercises

6. 📊 Write a program that prints minimum and maximum of five numbers entered by the user

7. 📅 Write a program to check if the year entered by the user is a leap year or not.

8. 🔢 Write a program to generate the sequence: –5, 10, –15, 20, –25... upto n, where n is an integer input by the user.

9. ∑ Write a program to find the sum of 1 + 1/8 + 1/27...1/n³, where n is the number input by the user.

10. 🔢 Write a program to find the sum of digits of an integer number, input by the user.

11. ↔️ Write a function that checks whether an input number is a palindrome or not.

## 12. Pattern Programming
Write a program to print the following patterns:

### (i) Diamond Pattern
```
       *
      * *
     * * *
    * * * *
     * * *
      * *
       *
```

### (ii) Right Triangle
```
  *
  * *
  * * *
  * * * *
```

### (iii) Inverted Right Triangle
```
  * * * *
  * * *
  * *
  *
```

### (iv) Number Triangle
```
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

### (v) Symmetrical Number Pattern
```
5 4 3 2 1 2 3 4 5
```

---
*Note: Practice these questions to strengthen your understanding of flow control in Python.*

