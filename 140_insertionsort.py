# IN insertion sort we assume that our 1st element is sorted.
def insertin_sort(priti):
    for i in range(1,len(priti)):
        j=i
        while priti[j]<priti[j-1] and j>0:
            temp=priti[j]
            priti[j]=priti[j-1]
            priti[j-1]=temp
        #priti[j-1]>priti[j] and j>0:
          # priti[j-1],priti[j]=priti[j],priti[j-1]
        j=j-1
priti=[2,8,4,6,9,1]
print('before sorting')
print(priti)
insertin_sort(priti)
print('after sorting')
print(priti)



