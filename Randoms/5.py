#Roll a dice 20 times using a random function.
#Store the frequency of each dice number (1–6) in a dictionary.
#Display the final frequency table in a readable format.
#Add a simple probability forecast based on the previous rolls
#each dice roll is independent, the probability of the next number is always 1/6 (uniform distribution). However, we can show the relative frequency of each number so far, which can give an idea of the "trend".
#**Output - **
import random
print("***welcome to roll a dice***")
stu={}
lst=[]
for i in range(1,21):
    guess=random.randint(1,6)
    lst.append(guess)

for i in lst:
    if i not in stu:
        stu[i]=lst.count(i)
print(stu)

print("1:",stu[1]*"*","(",stu[1],"times )")
print("2:",stu[2]*"*","(",stu[2],"times )")
print("3:",stu[3]*"*","(",stu[3],"times )")
print("4:",stu[4]*"*","(",stu[4],"times )")
print("5:",stu[5]*"*","(",stu[5],"times )")
print("6:",stu[6]*"*","(",stu[6],"times )")
print()
print("**Forecast (Relative Frequencies)**")

print("1:",(stu[1]/20)*100,"%","chance (based on past 20 rolls)")
print("2:",(stu[2]/20)*100,"%","chance (based on past 20 rolls)")
print("3:",(stu[3]/20)*100,"%","chance (based on past 20 rolls)")
print("4:",(stu[4]/20)*100,"%","chance (based on past 20 rolls)")
print("5:",(stu[5]/20)*100,"%","chance (based on past 20 rolls)")
print("6:",(stu[6]/20)*100,"%","chance (based on past 20 rolls)")
