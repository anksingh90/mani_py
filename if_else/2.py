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