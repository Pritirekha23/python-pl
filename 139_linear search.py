# python program for linear search
#LINEAR SEARCH:-
   # It is also called sequential search.
   


def linear_search(l,key):
    for i in range(len(l)):
        if (l[i]==key):
            return i
    return -1
l=[3,6,8,22,77]
key=8
#n=len(l)
result=linear_search(l,key)
if(result==-1):
    print("search fail")
else:
    print("search success and element is found at index:",result)