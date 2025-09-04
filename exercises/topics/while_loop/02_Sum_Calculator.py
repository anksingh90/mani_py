# Sum Calculator Using While Loop
# This program calculates the sum of integers from 0 to 10 using a while loop

# Initialize sum accumulator to store the total
sum = 0

# Initialize counter variable to start from 0
i = 0

# While loop continues as long as i is less than or equal to 10
while i <= 10:
    # Add current value of i to the running sum
    sum = sum + i
    
    # Increment counter by 1 to move to next number
    i = i + 1

# Display the final calculated sum
print(sum)

# Loop execution breakdown:
# Iteration 1: i=0, sum = 0+0 = 0, i becomes 1
# Iteration 2: i=1, sum = 0+1 = 1, i becomes 2
# Iteration 3: i=2, sum = 1+2 = 3, i becomes 3
# Iteration 4: i=3, sum = 3+3 = 6, i becomes 4
# Iteration 5: i=4, sum = 6+4 = 10, i becomes 5
# Iteration 6: i=5, sum = 10+5 = 15, i becomes 6
# Iteration 7: i=6, sum = 15+6 = 21, i becomes 7
# Iteration 8: i=7, sum = 21+7 = 28, i becomes 8
# Iteration 9: i=8, sum = 28+8 = 36, i becomes 9
# Iteration 10: i=9, sum = 36+9 = 45, i becomes 10
# Iteration 11: i=10, sum = 45+10 = 55, i becomes 11
# Loop ends when i=11 (condition i<=10 becomes false)

# Mathematical verification: Sum = 0+1+2+3+4+5+6+7+8+9+10 = 55
# Formula: Sum of first n natural numbers = n(n+1)/2
# For 0 to 10: Sum = 10(10+1)/2 = 10×11/2 = 55

# Final output: 55

'''
sum=0
i=0
while i<=10:
   sum=sum+i
   i=i+1
print(sum)
'''