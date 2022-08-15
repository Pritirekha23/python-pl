# sum of n natural numbers
def sumofnt(n):
    if n==1:
        return n
    return n+sumofnt(n-1)
print(sumofnt(3))