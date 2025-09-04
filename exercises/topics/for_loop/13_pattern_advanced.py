"""
Program: Advanced Pattern Printing
Description: Complex pattern printing using nested loops

Topics covered:
1. Complex patterns
2. Multi-level nesting
3. Advanced formatting

Learning Outcomes:
- Advanced pattern logic
- Complex nested loops
- Pattern optimization
"""

# printing 2d matrix(3*2)values in python 
matrix=[[1,2,3],[4,5,6]]

for row in matrix:
    for coloumbs in row:
        print(coloumbs,end=' ')
    print('')

