def star(n):
    print('*'*n)
    if n==5:
        return
    star(n+1)
star(1)   