def numb(n):
    print('#'*n)
    if n==1:
        return
    numb(n-1)
numb(5)
