# Class 11 | CS Test

## Multiple Choice Questions

### 1. Which loop is best if iterations known?
a) while loop  
b) for loop  
c) do while loop  
d) infinite Error

---

### 2. What will be the output of the following code:
```python
x = "python"
y = "hello"
print(y + x)
```

a) "python hello"  
b) "hello python"  
c) "pythonhello"  
d) "hellopython"

---

### 3. What is the output of the following python code:
```python
if 1:
   print("Not Empty")
else:
   print("Empty")
```

a) Not Empty  
b) Empty  
c) 1  
d) Error

---

### 4. What is the output of the following python code:
```python
n=2
while n<7:
  print(n,end=" ")
  n+=2
```

a) 2 4 6  
b) 2 4 6 7  
c) 2 7  
d) Infinite loop

---

### 5. Which statement is used to skip the current iteration in a loop?
a) break  
b) continue  
c) pass  
d) exit

---

## Programming Questions

### 6. Error Correction
Mehak, a Python programmer, wants to print the squares of all odd numbers between 1 and 20. She wrote the following code, but it contains errors. Correct the code and underline the corrections made.

```python
num = 1
while num < 20
   if num % 2 = 1
   print(num*2)
   num += 1
```

---

### 7. Number Classification Program
Write a program in python that takes a number as an input from the user and check whether that number is positive, negative, or zero.

---

### 8. Expression Evaluation
What will be the output of following statement:
```python
2**3**2+10-2
```

---

### 9. Nested Loop Output
What is the output of the following code?
```python
for i in range(2,5):
	for j in range(1,i+1):
		print(j,end="")
	print()
```

---

### 10. Prime Number Checker
Write a Python program that takes an integer input from the user and checks whether the number is prime or not.

---

### 11. Series Sum Program
Write a program in python to input the value of x and n and print the sum of the following series:

-x + (x²)/2 - (x³)/3 + (x⁴)/4 ... + (xⁿ)/n

---

### 12. String Reversal Output
What is the output when following code is executed?
```python
>>>str="kendriya"
>>>str[::-1]
```

---

### 13. Tuple Element Access
Suppose a tuple T1 is declared as:
```python
T = [10, 20, 30, 40, 50,(1,'a',3),'b']
```
Which of the following statement will print 'a'?

---

### 14. String Iteration Output
Write the output of the following code:
```python
S="Kendriya"
for i in range(len(S)):
  print(S[i],end="@")
```

---

### 15. Error Correction - String Operations
Observe the following Python code very carefully and rewrite it after removing all errors with each correction underlined.
```python
Str='Jagdalpur"
L= length(Str)
For j in range(L)
  Print(j)
```

---

### 16. Loop Iteration Count
How many times "Hello KV" will be printed after the execution of the following code:
```python
for x in range(0,20,2):
   print('Hello KV')
print('Hello KV'*2)
```

---

### 17. Dictionary Operations
Predict the output.
```python
d1={1:'Mon',2:'Tue',3:'Wed',4:'Thur',5:'Fri',6:'Sat',7:'Sun'}
d2=d1.copy()
d3=d2
d2[2]='TUE'
print(d1[2],d2[2],d3[2])
```

---

### 18. Employee Incentive Calculator
Write a program to accept sales of n (accept value of n from user) employees of a company.
Calculate the incentive to be given based on the following criteria:

| Incentive | Sales |
|-----------|-------|
| 10% of sales | > 100000 |
| 7% of sales | 75000 to 100000 |
| 5% of sales | < 75000 |

---

### 19. Diwali Discount Program
Write a program for Big Store's Diwali festival offers:
- a. sales >= 5000, the discount will be 20% of the sales
- b. 1000 < sales < 5000, the discount is 10%
- c. 500 < sales < 1000, the discount is 5%
- d. sales < 500, no discount

---

**End of Test**
