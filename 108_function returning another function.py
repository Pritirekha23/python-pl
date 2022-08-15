#function returning another function


print('ex-1-------')
def out():
    print("hello outer")
    def inner():
        print("Hi inner")
    print("*****")
    return inner
out()
y=out()

y()
#This is way to call inner function by outside of the outer function .here y means inner()


print("ex-2------------")
def fun1(abc):
    print('abc id is',id(abc))
    return abc
def x():
    print('x id is',id(x))
    print('python is so popular now')

#here abc ,data , x all are same 

data=fun1(x)
data()
print('data id is',id(data))
