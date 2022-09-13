# filter using lambda
  # It is a library function.
  # filter() is a function is used to filter value from a sequece.
  # It is a higher order function(If a function take function as an argument) .
  # we cant predict the output
# ex-1
# WAP TO FILTER ALL THE EVEN VALUE FROM A COLLECTION
print(' filter functions without using lambda')
def checkeven(x):
    if x%2==0:
        return True
    else:
        return False
l=[2,4,6,5,4,43,26,7,88,99,42]
#help(filter())
data=filter(checkeven,l)
for i in data:
    print(i)
print(type(data))
# storing or saving
# we can convert that filter data into list ,tuple ,set etc
print('list data')
data=list(filter(checkeven,l))
print(data)
print(type(data))

print('tuple type')
data=tuple(filter(checkeven,l))
print(data)
print(type(data))


print('filter function with using lambda')
l=[12,3,4,6,5,9,67]
data=list(filter(lambda x:x%2==0,l))
print(data)

# WITH USING LAMBDA IN ONE LINE 
# The drawback is that if i want to print it multiple times then we have to write it again.
# not storing or not saving
print('in one line')
print(list(filter (lambda x:x%2==0,[12,34,54,66,7,4])))


#x=2
# WAP TO FILTER ALL THE odd VALUE FROM A COLLECTION
print('filter odd number in list ')
print(list(filter (lambda x:x%2!=0,[12,34,54,66,7,3,13,77,4])))

print('filter odd number in tuple  ')
print(tuple(filter (lambda x:x%2!=0,(12,34,54,66,7,3,13,77,4))))


#ex-3
#FILTER ALL THE NEGATIVE VALUE FROM A SEQUENCE USING FILTER

print('all the -ve number')
t=(12,-4,-67,4,6,-87)
da=tuple(filter(lambda y:y<0,t))
print(da)

print('all the +ve number')
t=(12,-4,-67,4,6,-87)
da=tuple(filter(lambda y:y>0,t))
print(da)

#in one line
print('in one line')
print(tuple(filter(lambda y:y<0,(12,-3,4,-6,))))
print(tuple(filter(lambda y:y>0,(7,-6,-5,-4,3,2,1))))


# FILTER OUT ALL THE COMMON ELEMENT FROM BOTH LIST USING FILTER FUNCTION
print('common element in both two list')
l1=[12,33,56,76,34]
l2=[33,56,20,12,77]
data=list(filter(lambda x:x in l1,l2))
print(data)

print('in one line common element')
print(list(filter(lambda x1:x1 in (12,3,4,2),(5,12,24,2,33))))

# filter only one name smruti from a list using filter function
print('-----')
name=['priti','smruti','jyoti','smruti','msmi']
data=list(filter(lambda x:x=='smruti',name))
print(data)
print('--******--')
name=['priti','smruti','jyoti','smruti','msmi']
data=list(filter(lambda x:x!='smruti',name))
print(data)
print('1 - line')
print(list(filter(lambda x1:x1=='smruti' , ['priti','smruti','jyoti','smruti','msmi'],)))


#print all the even roll number names
print('dict-----')
d={
    1:'surendra',2:'priyanka',3:'kk',4:'Kim namzoon',5:'jungkook'
    
}
print(d)
print(d.items()) # it will give all the element
daa=dict(filter(lambda x:x[0]%2==0,d.items()))
print(daa)
print(d.items())

print('---')
#daa=dict(filter(lambda x:x[0]%2==0,d.keys()))
print(daa)  #TypeError: 'int' object is not subscriptabl --- > d.keys means only it will return key values so  convert it into list bcz these are the individual elemets not the key elements

daa=list(filter(lambda x:x%2==0,d.keys()))
print(daa)


# filter is important for INTERVIEW

















