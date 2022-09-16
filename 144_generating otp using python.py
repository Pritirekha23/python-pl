# dt-14-09-22
# Generating otp using python

import random
# creation of 4 digit otp
print(random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),sep='')
# sep='' -> to ignore the space

# Generating 4 digit otp using loop

otp=''
for i in range(4):
    otp=otp+str(random.randint(0,9))
print(otp)

print('-------')
# 0000- it will treat as single 0 so  here we get the value in between 0 to 9999
d=random.randint(0000,9999)
print(d)


d=random.randint(1000,9999)
print(d)








