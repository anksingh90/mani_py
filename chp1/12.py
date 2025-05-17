'''
wap to check if a person is eligible for a loan
ask for age,income,any loan
age less than 21=not eligible
greatr than 21 
    ai=less than 30000
        not eligible
    ai=greatr than 30000
        exixting loan=yes(eligible for 50% of loan) 
        no loan=yes(100% of loan)
    loan amt=3*ai           
'''
age=int(input("Enter your age"))
annual_income=int(input("Enter your income"))
loan=input("any existing loan :y/n ")
loan_amt=3*annual_income
if age>21:
    if annual_income>30000: 
        if loan=="y":
            print("loan available: ",loan_amt*0.5)
        else:
            print("no loan:",loan_amt*1)
    else:
        print("not eligible")        
else:
    print("under age not eligible")            

    








