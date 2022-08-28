#WAP TO SWAP THE TWO NUMBER IN A LIST
def swap(list,p1,p2):
    list[p1],list[p2]=list[p2],list[p1]
    return list
list=[122,3,45,56,76]
p1,p2=1,4
print(swap(list,p1-1,p2-1))