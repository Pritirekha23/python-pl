# Recursion in python
 # if a function call itself it is called as recursion.
 # Recursion must have a base case(termination condition) and recursive steps.
 #Advantages :-
  # To solve the complex problem easily .
  # To write less code/concise code
  # Recursion will increase the readability of the code.

#print  number from 1 to 5 using recursion and without recursion
#without recursion
print('withou recursion ex')
for i in range(1,6):
    print(i)


print('using recursion ex-')
def fun(n):
    if n==6:
      return
    else:
     print(n)
     fun(n+1)


fun(1)

print('ex-2')

def fun(n):
    if n==3:
      return
    else:
        fun(n+1)
        print(n)
fun(1)
     












