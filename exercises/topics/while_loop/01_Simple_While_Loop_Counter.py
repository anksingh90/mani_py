# Simple While Loop Counter
# This program demonstrates a basic while loop that prints numbers from 0 to 4

# Initialize counter variable to 0
i = 0

# While loop continues as long as i is less than 5
while i < 5:
    # Print the current value of counter
    print(i)
    
    # Increment counter by 1 to avoid infinite loop
    # This ensures the loop condition will eventually become false
    i = i + 1

# Loop execution breakdown:
# Iteration 1: i=0, prints 0, i becomes 1
# Iteration 2: i=1, prints 1, i becomes 2  
# Iteration 3: i=2, prints 2, i becomes 3
# Iteration 4: i=3, prints 3, i becomes 4
# Iteration 5: i=4, prints 4, i becomes 5
# Loop ends when i=5 (condition i<5 becomes false)

# Output will be:
# 0
# 1
# 2
# 3
# 4

'''
i=0
while i<5:
    print(i)
    i=i+1
'''