# make a password with combination of 2 lower char, 2 upper char, 2 special chara, 2 numbers.
# aaAA12@#

import random
for i in range(0,2):
    print(chr(random.randint(65,90)), end = '')
    print(chr(random.randint(97,122)),end='')
    print(chr(random.randint(32,64)),end='')
    print(random.randint(0,9),end='')
print( )