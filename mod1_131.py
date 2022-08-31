
def add(a,b):
    print(a+b)

#check
if __name__=='__main__':
    add(1,3)
    print(__name__)
else:
    print('mod1_131 executed indirectly')

print('----')

def sub(x,y):
    print(x-y)
print(__name__)