# math module
import math
#print(help(math))
#print(dir(math))
print(math.pi)

#area of circle
area=math.pi*3.5*3.5
print(area)

print(math.e)

#Working with different functions
print('ceil')
print(math.ceil(2.1))
print(math.ceil(4.0))
print(math.ceil(4.9))
print('floor')
print(math.floor(2.1))
print(math.floor(4.0))
print(math.floor(4.0))

print(math.sqrt(144))
print(math.floor(math.sqrt(144)))

print(math.factorial(5))

#removing -by default the output will be in float foramt
print(math.fabs(-2))
print(math.fabs(2))
print(math.fabs(3.5))
print(math.fabs(10))




#you will get the output of reminder
print(math.fmod(10,2))
print(math.fmod(10,3))
# if u want to print the int part then
print(math.floor(math.fmod(10,3)))

#fsum- sum of the  numbers
print(math.fsum([12,43,56,7,5,6]))
print(math.floor(math.fsum([12,43,56,7,5,6])))