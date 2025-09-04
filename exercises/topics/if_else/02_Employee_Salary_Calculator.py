# Employee Salary Calculator
# Calculate total salary of employee based on hours worked daily
# Rules:
# - If worked 8 hrs daily: no incentive
# - If worked 8.5 hrs daily: 15% of salary as incentive
# Total salary formula: sal + da + hra
# Where: da = 20% of salary, hra = 120% of salary

# Get daily working hours from user
a = int(input("Enter the number of hours worked "))

# Check for standard 8-hour workday
if a == 8:
    # No incentive for standard 8-hour work
    
    # Get base salary from user
    sal = int(input('Enter your salary : '))
    
    # Calculate allowances
    da = sal * 0.2      # Dearness Allowance: 20% of salary
    hra = sal * 1.20    # House Rent Allowance: 120% of salary
    
    # Calculate total salary (base + allowances, no incentive)
    total_sal = sal + da + hra
    
    # Display final salary
    print('Total Salary : ', total_sal)

# Check for 8.5-hour workday (overtime)
elif a == 8.5:
    # Should include 15% incentive for 8.5-hour work (but not implemented in calculation)
    
    # Get base salary from user
    sal = int(input('Enter your salary : ')) 
    
    # Calculate allowances
    da = sal * 0.2      # Dearness Allowance: 20% of salary
    hra = sal * 1.20    # House Rent Allowance: 120% of salary
    
    # Calculate total salary (base + allowances)
    # Note: Missing 15% incentive calculation as mentioned in requirements
    total_sal = sal + da + hra 
    
    # Display final salary
    print('Total Salary :', total_sal)

# Note: Program doesn't handle other working hour values
# Missing: 15% incentive calculation for 8.5-hour case
# Missing: Error handling for invalid hour inputs

'''
# calculate salary(sal) of employee, ask for total number of hours worked weekly.
# if worked 8 hrs daily, then no incentive, if worked 8.5 hrs daily then 15% of salary as incentive. 
# total_sal = sal + da + hra (da = 20% of sal, hra = 120% of sal).

a=int(input("Enter the number of hours worked "))

if a==8:
    sal = int(input('Enter your salary : '))
    da = sal * 0.2
    hra = sal * 1.20
    total_sal = sal + da + hra
    print('Total Salary : ',total_sal)
elif a==8.5:
    sal=int(input('Enter your salary : ')) 
    da= sal*0.2
    hra =sal *1.20
    total_sal= sal + da + hra 
    print('Total Salary :',total_sal)
'''