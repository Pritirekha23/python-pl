# dt-13-09-22
# Number guessing game in python


import random
rn=random.randint(1,10)
count=0
#print(rn)
while True:
  count=count+1
  choice=int(input('Guess a number in between 1 to 10::'))
  if choice==rn:
    print('congrts! ur guess is correct')
    break
  elif choice>rn:
    print(' sorry ur guess number is greater than system generated number')
  else:
    print(' sorry ur guess number is less than system generated number')

print(f'u have taken {count} steps to guess the number')