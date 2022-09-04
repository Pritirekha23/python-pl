# Wap to swap two numbers in python
print('way-1')
n1=input('Enter the first number')
n2=input('Enter the second number')
temp=n1
n1=n2
n2=temp
print('The value of n1 after swapping',n1)
print('The value of n2 after swapping',n2)

print('way-2')
n1=input('Enter the first number')
n2=input('Enter the second number')
n1,n2=n2,n1
print('The value of n1 after swapping',n1)
print('The value of n2 after swapping',n2)
