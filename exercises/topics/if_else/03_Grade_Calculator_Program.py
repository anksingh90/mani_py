# Grade Calculator Program
# This program assigns grades based on student marks using conditional statements

# Get student marks from user input
marks = int(input("Enter your marks : "))

# Grade assignment based on marks range
# Check for Grade A: marks between 90-100 (inclusive)
if marks <= 100 and marks >= 90:
    print('Grade : A')

# Check for Grade B: marks between 80-89 (inclusive)
elif marks <= 89 and marks >= 80:
    print('Grade : B')

# Note: Program is incomplete - missing grade ranges for lower marks
# No handling for:
# - Marks below 80 (Grade C, D, F, etc.)
# - Invalid marks (negative numbers, marks > 100)
# - Non-numeric input validation

# Current grading system implemented:
# A: 90-100
# B: 80-89
# Ungraded: below 80 or above 100

'''
marks=int(input("Enter your marks : "))

if marks<=100 and marks>=90:
    print('Grade : A')
elif marks<=89 and marks>=80:
    print('Grade : B')
'''