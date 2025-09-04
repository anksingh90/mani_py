"""
Program: Fibonacci Series
Description: Generate Fibonacci sequence using loops

Topics covered:
1. Fibonacci sequence
2. Series generation
3. Number patterns

Learning Outcomes:
- Sequence generation
- Mathematical patterns
- Variable manipulation
"""

num = 1
for i in range(1,5):
    for j in range(i):
        print(num, end=' ')
        num = num + 1
    print('')


