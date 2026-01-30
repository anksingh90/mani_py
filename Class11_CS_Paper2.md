# Class 11 | CS Paper 2

---

## 1. Dictionary Methods Output

Write the output for the following codes:

```python
A = {10:1000, 20:2000, 30:3000, 40:4000, 50:5000}
print A.items()
print A.keys()
print A.values()
```

---

## 2. Error Detection - Dictionary Input

Find errors from the following codes:

```python
c = dict()
n = input(Enter total number)
i = 1
while i <= n
    a = raw_input("enter place")
    b = raw_input("enter number")
    c(a) = b
    i = i + 1
print "place", "\t", "number"
for i in c:
    print i, "\t", cla[i]
```

---

## 3. List Expression Evaluation

For each of the expression below, specify its type and value. If it generates error, write error.

Assume that expressions are evaluated in order.

```python
x = [1, 2, [3, 'abc', 4], 'Hi']
```

(i) `x[0]`

(ii) `x[2]`

(iii) `x[-1]`

(iv) `x[0:1]`

(v) `2 in x`

(vi) `x[0] = 8`

---

## 4. Type and List Declaration

What is the output of the following code:

a) 
```python
print type([1, 2])
```

b) 
```python
a = [1, 2, 3, None, (), []]
```

---

## 5. List Sum Calculation

Write the output from the following code:

```python
A = [2, 4, 6, 8, 10]
L = len(L)
S = 0
for I in range(1, L, 2):
    S += A[I]
print "Sum=", S
```

---

## 6. Error Detection - List Input

Find the errors from the following program:

```python
n = input(Enter total number of elements)
l = range(n)
print l
for i in (n);
    l[i] = input("enter element")
print "All elements in the list on the output screen"
for i on range(n):
    print l[i]
```

---

## 7. Name and Phone Number Dictionary

Write a Python program to input 'n' names and phone numbers to store it in a dictionary and print the phone number of a particular name.

---

## 8. Cumulative Sum Function

Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list where the i<sup>th</sup> element is the sum of the first i+1 elements from the original list. 

For example, the cumulative sum of `[1, 2, 3]` is `[1, 3, 6]`.

---

***** END *****
