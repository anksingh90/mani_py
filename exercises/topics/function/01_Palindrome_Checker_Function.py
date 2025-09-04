# Palindrome Checker Function
# Note: Function name suggests vowel counting but actually checks for palindromes

def vowel_count():
    """
    Function to check if a string is a palindrome
    A palindrome reads the same forwards and backwards
    """
    
    # Define the test string with spaces at beginning and end
    s = " kanak "
    
    # Create reversed version using slice notation [::-1]
    # This reverses the entire string including spaces
    s1 = s[::-1]
    
    # Compare original string with reversed string
    if s == s1:
        # If strings match, it's a palindrome
        print("this is a palindrome")
    else:
        # If strings don't match, it's not a palindrome
        print("this is not a palindrome")

# Call the function to execute the palindrome check
vowel_count()


'''
def vowel_count():


    s=" kanak "
    s1=s[::-1]
    if s==s1:
        print("this is a palindrome")
    else:
        print("this is not a palindrome")

vowel_count()'''