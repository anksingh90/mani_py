# Mean Calculator Function
# This program calculates and displays the mean (average) of a predefined list

def mean():
    """
    Function to calculate mean of the list [1.4, 2.4, 3.5, 6.9, 7.3, 1.4]
    Uses hardcoded sum (22.9) and count (6) instead of dynamic calculation
    Mean formula: sum of all values / number of values
    """
    # Calculate mean using hardcoded values
    # 22.9 is the sum of all elements in the list
    # 6 is the total number of elements in the list
    s = 22.9 / 6 
    
    # Display the calculated mean
    print(s)  

# Define the list of numbers for which mean is calculated
# Sum of elements: 1.4 + 2.4 + 3.5 + 6.9 + 7.3 + 1.4 = 22.9
# Number of elements: 6
lst = [1.4, 2.4, 3.5, 6.9, 7.3, 1.4]

# Call the mean function to calculate and display result
# Note: The function doesn't use the 'lst' variable - it uses hardcoded values
mean()

'''
def mean():
    s=22.9/6 
    print(s)  

lst=[1.4,2.4,3.5,6.9,7.3,1.4]

mean()
'''