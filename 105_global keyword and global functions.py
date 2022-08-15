#Global keyword and globals[] functions
#global keyword
 #If u want to create global variable inside a function then u have to use global keyword
 


print('global keyword ex-1')
def fun():
    global A
    A=54 #global variable
    b=9 #local variable
    print(A)
    print(b)
def fun1():
    print(A)
    
fun()
fun1()

#By using global keyword we can perform modification on global variable inside function .

print('global keyword ex-2')
A=22 #global variable
def fun():
   # print(A) #SyntaxError: name 'A' is used prior to global declaration
    print('A')
    global A
    A=54 #global variable(updated)
    print(A)
   
def fun1():
    print(A)
fun()
fun1()


print('global keyword ex-3')
def fun():
   # A=6 #dont create local variable with same Global var name .. if u create the it will produce an error
   # print(A)
    b=8
    print(b)
    global A
    A=54 #global variable
    b=9 #local variable
    print(A)
    print(b)
def fun1():
    print(A)
fun()
fun1()

#global function
 # If ur local var and global var name is same at that time if u want to access global variables then u have to use global functions.
print('global function ex-1')
a=23
def priti():
    #local variable is having more priority/scope than global variables.thats why its printing 999
     
     #but  if u want to print that global variable then at that time u have to use global functions.
    a=999
    print(a)
    print(globals()['a'])


priti()

print('global function ex-2')
a=6
def fun():
    a=777
    print(a)
    data=globals()['a']
    print(data)
fun()
print(a)
#print(data)# u cant print data here bcz it is a type of local var which is created inside a function . if u try to access then u will get an error





