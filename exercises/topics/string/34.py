#wap that reads a line then count how many times "is" apear in the line and display the line
count=0
str='This is a string!'

for i in str.split():
    if 'is' == i:
        count = count + 1

print(count)