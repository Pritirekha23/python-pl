# INTRODUCTION OF MODULE
 # reqirement of module
   # If we wannt to reuse the code we can go for functions,but if we want to reuse group of variables,function and classes then we can go for module.
# Module means collection of classes ,variables and functions and everything store .py file.
# Each and evry .py file is called module.


import Hellocal122   # here we are importing Hellocalmmodules that means we can access all the members of Hellocal modules.
print('hellocal122')
print(Hellocal122.add(2,3))
print(Hellocal122.sub(100,20))
print(Hellocal122.pi)


  # TYPES OF MODULE
  #1> Standard module
  #2> User defined modules
  #3> 3rd party modules

#1> Standard module-(predefined /in-build in)
# already created.
     # Those module which is offcially provided by python and these modules are available inside python software. Ex-os,sys,math etc
print('---math mod--')
import math
print(math.factorial(3))


#2> User defined modules
  # The module which is created by user as per our requirement such type of module is called as user defind module.
  #ex-hellomath,cal etcs

print('---cal mod--')

#3> 3rd party modules
 # These module provided by 3rd party vendor,it is available on internet so we have to download it by using pip.
 #ex- NumPy,pandas,matplitib etc





#MODULE AND ITS MEMBER ALIASING
# giving another name to module is called module aliasing.

# module aliasing
#way-4
import Hellocal122 as h  # here we are giving the alias name to Hellocal122_123 as h so we can now acess data by aloas name also
print('123hellocal122')
print(h.add(2,3))
print(h.sub(100,20))
print(h.pi)
print(Hellocal122.pi)

#DIFFERENT WAYS OF IMPORTING MODULES  ALIASING
#1 way
print('--way1--')
from Hellocal122 import add
#here we can acess only add function we cant access sub bcz it is not degfined
print(add(2,4))

#print(sub(7,3)) #error
#2 way
print('--way2--')
from Hellocal122 import add,sub,mul
print(add(2,4))
print(sub(3,2))
print(mul(2,4))

print('--way3--')
#here we can access everything from Hellocal122_123
from Hellocal122 import*
print(add(2,4))
print(sub(3,2))
print(mul(2,4))
print(pi)




# module members aliasing
print('member alising')
from Hellocal122 import add as a
print(a(2,3))

print('---')
from Hellocal122 import add as a,sub as s, pi as p,mul as m
print(a(2,4))
print(s(2,1))
print(m(3,2))
print(pi)
print(p)






































