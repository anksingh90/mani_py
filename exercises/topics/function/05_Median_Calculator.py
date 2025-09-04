# 05.py - Median Calculator
# This script demonstrates finding the middle position of a sorted list

def median(lst):
    """
    Function to find and display median information of a list
    Args: lst - list of numeric values
    """
    # Calculate middle position based on list length
    if len(lst)%2==0:
        middle_value = len(lst)/2          # Even length: divide by 2
    else:
        middle_value = (len(lst)+1)/2      # Odd length: add 1 then divide by 2

    # Sort the list in ascending order (modifies original list)
    lst.sort()
    
    # Display sorted list
    print(lst)
    
    # Display the calculated middle position (converted to int, adjusted by -1)
    print("The middle value of the list",int(middle_value) -1)
    
    # Access the element at middle position (result not stored or returned)
    lst[middle_value]

# Main Program - Test the median function
lst=[1.4,2.4,3.5,6.9,7.3,1.4]    # Test list with 6 elements
median(lst)                        # Call median function