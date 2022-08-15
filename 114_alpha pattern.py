#alpha pattern using loop
print('----Example---1')
def alphap(n):
    s="ABCDEfghi"
    for i in range(1,n+1):
        for j in range(i):
            print(s[j],end=' ')
        print()
alphap(5)


print('----Example---2')
def alphap(n):
    s="ABCDEfghi"
    for i in range(5,n-1):
        for j in range(i):
            print(s[j],end=' ')
        print()
alphap(1)






