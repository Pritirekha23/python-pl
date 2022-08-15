#star pattern--

print('---Example---1')
def star(n):
    print('*'*n)
    if n==5:
        return
    star(n+1)
star(1)   

print('---Example---2')
def star(n):
    print('*'*n)
    if n==1:
        return
    star(n-1)
star(5)




