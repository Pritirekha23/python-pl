# generate fake students data


# generate student name
  
from random import*

alpha="abcdefghijklmnopqrstuvwxyz"
sname=''
for i in range(6):
    sname=sname+choice(alpha)
print(sname)

# it always print 6 charcter name


print('-------------')
# here we gave the range through randint so the name is between 3 to 12 character
alpha="abcdefghijklmnopqrstuvwxyz"
sname=''
for i in range(randint(3,12)):
    sname=sname+choice(alpha)
print(sname)


print('----name----')
alpha="abcdefghijklmnopqrstuvwxyz"
for i in range(10):
    sname=''
    for i in range(randint(3,12)):
       sname=sname+choice(alpha)
    print(sname)

print('-------first name with last name-----')
alpha="abcdefghijklmnopqrstuvwxyz"

for i in range(10):
   fname=''
   lname=''
   for i in range(randint(3,12)):
    fname=fname+choice(alpha)
    lname=lname+choice(alpha)
   print(fname,lname)


print('-------first name 1st character in capital and last name 1st character in capital-----')
alpha="abcdefghijklmnopqrstuvwxyz"

for i in range(10):
   fname=choice(alpha).upper()
   lname=choice(alpha).upper()
   for i in range(randint(3,12)):
    fname=fname+choice(alpha)
    lname=lname+choice(alpha)
   print(fname,lname)
# student mobile number
print('---mob number--')
digit='0123456789'
s_mobno=choice('9876')
for i in range(9):
    s_mobno=s_mobno+choice(digit)
print(s_mobno)

print('---number----')
digit='0123456789'
for i in range(10):
    s_mobno=choice('9876')
    for i in range(9):
     s_mobno=s_mobno+choice(digit)
    print(s_mobno)


# generate age
print('---age--')
for i in range(10):
    sage=randint(16,25)
    print(sage)


# generate address
print('--address--')
cities=['bbsr','bhadrak','cuttack','puri','ganjam']
for i in range(10):
    saddr=choice(cities)
    print(saddr)
    




# generate student id
print('---id-----')
digit='0123456789'
for i in range(20):
    sid='2001' # or sid='xyz'
    for i in range(6):
      sid=sid+choice(digit)
    print(sid)

# Generate branch
print('branch')
branch=['CSE','EE','ME',"CE"]
for i in range(10):
    sbranch=''
    sbranch=sbranch+choice(branch)
    print(sbranch)






