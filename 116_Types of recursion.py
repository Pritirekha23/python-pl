# Types of Recursion
 
# Direct recursion
# Indirect recursion
# Tail recursion
# Non-tail recursion(Head recursion)

# Direct recursion 
 #if a function call same function again , it is as direct recursion.
print('example of direct recursion--1')
def fun(n):
    if n==6:
      return
    else:
     print(n)
     fun(n+1)
fun(1)

# Indirect recursion
 # not-direct
  # if we have two functions fun1 and fun2,inside fun1 body we will call fun2 and inside fun2 body we will fun1 is called indirect recursion.
  # These  two functions are indirectly recursive bcz they call each other.


print('example of indirect recursion--1')

def fun1(n):
    if n<=5:
        print(f' fun1 = {n*2}')
        fun2(n+1)
    return

def fun2(n):
    if n<=5:
        print(f'fun2 = {n*100}')
        fun1(n+1)
    return
fun1(1)


# Tail recursion
  # it means last.
   # A function is said to be tail recursive if no operations are pending to perforemd when the recursive function return to its caller.
# A recursive function is called tail recursive if recursive is thelast thing doneby the function.

# NOTE-
  # There is no need to k``eep record of previous task.
print('example of tail recursion')
def fun(n):
    if n==3:
      return
    else:
     print(n)
     fun(n+1)
fun(1)

#Non-tail recursion(Head recursion)
 # A  function is said to be non-tail recursive if some operations are pending to perforemd when the recursive function return to its caller.
 # After returning back , there is something left to evaluate.

 # NOTE-
  # There is need to keep record of previous task .
print('example of non-tail recursion')
def fun(n):
    if n==3:
      return
    else:
     fun(n+1)
     print(n)
     
fun(0) 


















