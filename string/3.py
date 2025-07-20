str="hEllo world"
count=0
vowel="aeiouAEIOU"

for char in str:
    if char in 'aeiouAEIOU':
        count=count+1

print('Number of vowel in string : ',count)
