# Naming conflict  while importing  same member from different module
print('---')
import cal124
import data124
print(cal124.x)
print(data124.x)

#issues  are 

print('*****')
from cal124 import x
from data124 import x
print(x)

# Order is matter

print('===')
from data124 import x
from cal124 import x
print(x)


# SOLVE THE ISSUE
print('__')
from cal124 import x as a
from data124 import x as b
print(a)
print(b)











