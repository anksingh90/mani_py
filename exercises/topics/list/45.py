lst=[1,2,3,4,5]

mid_val = int((len(lst)/2))
for i in range(mid_val):
    lst[i], lst[mid_val + i] = lst[mid_val + i], lst[i]
print(lst)