"""
Program: Prime Numbers
Description: Prime number operations and checks using loops

Topics covered:
1. Prime number testing
2. Prime generation
3. Factor checking

Learning Outcomes:
- Prime number concepts
- Optimization techniques
- Mathematical logic
"""

for i in range(0,20,5):
    if i>0:
        if i%10==0:
            print(i)
        else:
            print("-",i)
        