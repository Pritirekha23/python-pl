def bin_search(list,key):
    low=0
    high=len(list)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
    if list[mid]<key:
        low=mid+1
    elif list[mid]>key:
        high=mid-1
    else:
        return -1

      
list=[33,44,55,66,77,88]
key=66
result=bin_search(list,key)
print(list)
if result!=-1:
    print('element is found at index{result}:')
else:
    print('element not found')





















print('----')
def binary_search(ar,l,r,y):
    if r>l:
        mid=l+(r-1)//2
        if ar[mid]==y:
            return mid
        elif ar[mid]==y:
            return binary_search(ar,l,mid-1,y)
        else:
              return binary_search(ar,mid+1,r,y)
    else:
        return-1

ar=[2,4,6,7,9,10]
y=9
result=binary_search(ar,0,len(ar)-1,y)
if result !=-1:
    print('element is present at index %d',result)
else:
    print('search fail')



