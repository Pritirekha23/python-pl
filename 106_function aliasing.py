# function aliasing
 #it means set another name to function .
# IF U WANT TO REUSE YOUR CODE THEN GO FOR FUNCTION

print('-------')
def calculations(a,b):
    print(a+b)   
    print(a-b)
    print(a%b)
    print(a*b)
calculations(20,5)
cal=calculations # we can call with the help of cal and calculations -- here cal is alias name
print('after aliasing')
cal(10,2)
cl=calculations
cl(4,2)


print('--------------')
def calculations(a,b):
    print(a+b)   
    print(a-b)
    print(a%b)
    print(a*b)
calculations(20,5)
cal=calculations
print(id(calculations))
print(id(cal))
del calculations
print('&&&&&')
cal(4,2)
#calculations(20,2) #NameError: name 'calculations' is not defined----we deleted this function





print('-------')
def calculations(a,b):
    print(a+b)   
    print(a-b)
    print(a%b)
    print(a*b)
calculations(20,5)

cal=calculations
cl=calculations
c=cl
cal(55,2)
cl(44,3)
print('aliasing of alias')
c(4,2)
print('id')
print(id(calculations))
print(id(cal))
print(id(cl))
print(id(c))







