#write a program that calculates equivalent energy using Einstein's famous equation:
# E = mc²

#where:
# E = Equivalent energy
# m = Mass of object
# c = Speed of light (≈ 3×10⁸ m/s)

#Input:** Mass of an object  
#Output:** Equivalent energy
m=int(input("Enter mass of an object"))
c=int(input("Enter equivalent energy of an object"))
E=m*c**2
print(E)