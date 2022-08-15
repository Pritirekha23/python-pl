#Fibonacci series using binary recursion
 # 0 1 1 2 3 5 8 13 21

# fibonacci series of 3 --> 0 1 1       2
      #              4-----> 0 1 1 2    3
    
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(4))
