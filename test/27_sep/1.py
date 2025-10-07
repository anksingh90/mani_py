#str = 'The quick brown fox jumps over the lazy sleeping dog outside in the bright warm sunshine 
# every morning'
#Ask user to enter a string
#a) Convert words to a list
#b) Count occurrences of the word 'in' in the list
#c) Reverse the list
#d) Clear all items from the list
count=0
str="The quick brown fox jumps over the lazy sleeping dog outside in the bright warm sunshine every morning"
str1=str[::-1]
for i in str:
    if "in" in i:
        count+=1
print(str1)        
print(count)        
