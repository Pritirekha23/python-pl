#reduce function in python
# It is used to reduce a sequence of elements into single element.
# Reduce function present inside functools,so we have to import it before reduce function.
# syntax
    # reduce(function,sequence)
      # function parameter-> it will reduce sequence of elements into a single element.
# THIS REDUCE FUNCTION Is BY DEFAULT NOT AVAAILABLE , SO WE HAVE TO  IMPORT IT

# It return the data based on the input data.

# find the sum of all element present inside list without using lambda
from functools import reduce
#without using lambda
print('reduce function')
def addall(x,y):
    return x+y
l=[1,2,3,4,5]
data=reduce(addall,l)
print(data)
print(type(data))


# when u call addall function this reduce will pass two value to x and y

#with using lambda
l1=[2,3,4,5]
var=reduce(lambda x,y:x+y,l1)
print(var)





print('in-one-line')
print(reduce(lambda x,y:x+y,[1,2,3,4,5,6]))


# product of all the element present inside list with using lambda
print('product-------')
l1=[2,3,4,5]
var=reduce(lambda x,y:x*y,l1)
print(var)

#third argument
l1=[2,3,4,5]
var=reduce(lambda x,y:x*y,l1,10)
print(var)

# findout the sum of all the element from 1 to 100
print('sum of 1 to 100')
var=reduce(lambda x,y:x+y,range(1,101))
print(var)

var=reduce(lambda x,y:x+y,range(1,5))
print(var)
#Working with list which containing string data
print('working with string')
name=['JM','RM','Jin','TAe']
v=reduce(lambda x,y:x+y,name)
print(v)

#hello will add in the beginning but we cant provide integer here
name=['JM','RM','Jin','TAe']
v=reduce(lambda x,y:x+y,name,'hello')
print(v)

# work with dictionary
print('dict1')
d={
    2:'Kim namzoon',
    3:'Jin',
    4:'Jungkook',
    5:'Tae'
}
r=reduce(lambda x,y:x+y,d.keys())
print(r)

print('dict2')
d={
    2:'Kim namzoon',
    3:'Jin',
    4:'Jungkook',
    5:'Tae'
}
r=reduce(lambda x,y:x+y,d.values())
print(r)

# IMMORTANT FOR INTERVIEW
#REDUCE VS ACCUMULATE
from itertools import accumulate
#help(accumulate)
#1st it will take the sequence then u can apply the logic
l=[1,3,4,5,6]
print(list(accumulate(l,lambda x,y:x+y)))
print(reduce(lambda x,y:x+y,l))







































