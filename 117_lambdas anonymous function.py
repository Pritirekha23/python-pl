# lambdas anonymous function
 # lambda function is also known as anonymous function.
 # If we declare a function without any name such type of nameless function is called as lambda function or anonymous function .
 # Normal function is define using def keyword and lambda function is define using lambda keyword.
 # The main uses of lambda function is justfor one time use (i.e instant use)

# ex=1
# addition of two numbers
print('without using lambda')
def add(a,b):
    return a+b
print(add(10,20))

print('with using lambda')
f=lambda a,b:a+b
print(f(10,30))
print(type(f))

#ex=2
# square of a number
print('without using lambda')
def sq(n):
    return n*n
print(sq(10))


print('with using lambda')
x=lambda n:n*n
print(x(10))

#ex=3
# find out the greatest number using 2 number
print('without using lambda')
def fun(a,b):
    if a>b:
        return a
    else:
        return b
print(fun(23,65))

print('with using lambda')
x=lambda a,b:a if a>b else b
print(x(498,66))

#ex=4
print('ex-4')
x=lambda a,b:a+a if a>b else b+b
print(x(4,6))


#NOTE-
  # Lambda return only one value (only one expression it will return)
  # Where normal function can return multiple value
print('normal function returning multiple value')
def fun(a,b):
    return a,b
print(fun(2,4))

print('Lambda return only one value')
#z=lambda a,b:a,b  #NameError: name 'b' is not defined
#print(z(2,4))


# lambda can return collection

l=lambda b,c:[2,3,56,7]
print(l(2,3))



y=lambda :'hii'
print(y())

t=lambda :'i love   ' +'     india  '
print(t())



# find out greatest number among 2 number using lambda within one line .
print((lambda a,b:a if a>b else b)(10,23))










# POINTS-
  # WHERE WE EXACTLY USE LAMBDA DFUNCTION.
    # sometimes we have to pass  function as an argument to another function, at that time we can go for lambda function.
    # It is mainly used with higher order functio filter(), map(),reduce()
    # Higher order function means if a function takes function as an argument such type of function is called as higher order function.









