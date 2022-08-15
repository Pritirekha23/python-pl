#factorial of a number
def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
print(fact(3))