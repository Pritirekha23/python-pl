# map() using lambda function

 # If u have one or more sequence of data and if u want to operation on each and every data then we can go for map() function.
 # if u want to perform an operations on each and every individual element of map function then map() function is used .
 # The output is completely depend upon the no. of element which is present inside the input data.
 # if the no. of input element is 6 then the output no. of element is 6.

# syntax
 # map(function,sequences)
   # function- used to operation on each and every data

#ex-1
# add 4 to each and every individual element present in a sequence
print('--Without using lambda--')
def add4(x):
    return x+4
l=[10,20,30]
data=list(map(add4,l))
print(data)

print('--using lambda--')
l=[12,14,16,0]
da=list(map(lambda x:x+4,l))
print(da)


#In one line
print('in one line--')
print(list(map(lambda x:x+4,[120,20,30,40])))


# ex-2
# find out square of each number present inside tuple using lambda
print('square of each elemnt')
t=(2,3,4,5,6)
dt=tuple(map(lambda x:x*x,t))
print(dt)



print('in one line find square')
print(tuple(map(lambda x:x*x , (2,3,4,5,6,7))))


#passing multiple sequences
# add individual element of both list using lambda
print('add two list')
l1=[3,5,6,7,8]
l2=[1,4,9,2,0]
dtt=list(map(lambda x,y:x+y,l1,l2))
print(dtt)

print('in one line adding two list')
print(list(map(lambda x,y:x+y,[1,2,3],[4,5,6])))

#NOTE-
# LIST 1 and LIST 2  length must be same or u will gate unexpected output.
 # If the length of the list are same then the output will be different.
print('----lngth--')
l1=[3,5,6,7,8]
l2=[1,4,9,2]
dtt=list(map(lambda x,y:x+y,l1,l2))
print(dtt)


# find the length of each words present inside a list(collection)
print('*****')
name=['smruti','priti','jyoti','tiki','raja','msmi','swati']
dr=list(map(lambda x:len(x),name))
print(dr)


print('in one line----->>>')
print(list(map(lambda x:len(x),['smruti','priti','jyoti','tiki','raja','msmi','swati'])))


name=['smruti','priti','jyoti','tiki','raja','msmi','swati']
dr=(map(lambda x:len(x),name))
for i in dr:
    print(i)
# this map type  object , and u cant print directly but u can iterate it or ucan apply loop
print(type(dr))


# find the length of each words present inside a string
msg='Today is my birthday'
s=msg.split(' ')
print(s)
dr=list(map(lambda x:len(x),s))
print(dr)




















