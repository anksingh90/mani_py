'''
Discount Eligibility: A store offers a discount based on the purchase amount.If
the purchase amount is $100 or more, the discount is 10%.If the purchase amount is
between $50 and $99 (inclusive), the discount is 5%. Otherwise, there is no discount.
Write a program that asks the user for the purchase amount and prints the applicable
discount percentage
'''
amt=int(input("Enter the amount of purchase : "))
if amt>=100:
    print("discount==10%")
elif amt>50 and amt<99:
    print("discount==5%") 
else:
    print("no discount")    

