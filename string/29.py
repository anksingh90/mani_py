o_sum, e_sum = 0,0
for i in range(100,501):
    if i%2==0:
        e_sum+=i
    else:
        o_sum+=i

print(e_sum)    
print(o_sum)