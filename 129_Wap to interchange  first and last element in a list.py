# WAP TO INTERCHANGE FIRST AND LAST ELEMENT IN A LIST
def sl(sl1):
    s=len(sl1)
    temp=sl1[0]
    sl1[0]=sl1[s-1]
    sl1[s-1]=temp
    return sl1
sl1=[2,3,4,5,6,7,8]
print(sl(sl1))
