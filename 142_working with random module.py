#  WORKING WITH RANDOM MODULE IN PYTHON
  # Introduction to random module
  # Different function of random module
  # Difference between those functions


# Introduction to random module
 # if we want to generate random value then we can use   random module .


# Different functions  of random module
 # randint() , random() , randrange() , shuffle(), unifrom() , sample() , choice()


#1) randint() :-> It will generate random integer number in between  the given two number (like here 1 to 10)
import random
print('randint function')
val=random.randint(1,10) # both 1 and 10 are included
print(val)

#2) random():-> It will generate a random float no in between 0 to 1 .
#-> it does not take any argument .

print('random function-------')
val=random.random()
print(val)


#print(dir(random))
#print(help(random))
#print(help(random.random))


#3) randrange() :-> It is same as randint but here stop value is not included .

# in this example 10 is not included
print('randrange function--------')
v=random.randrange(1,10)
print(v)


#4) shuffle():-> 
print('without shuffle')
# here we get in a proper order
l=[23,43,53,63,73,83,93]
print(l)

print('with shuffle funvtion-------')
# it is used in the music player
# here we get same value in different different position(any random manner)
l=[23,43,53,63,73,83,93]
random.shuffle(l)
print(l)


#5) unifrom():-> It will generate float value in between that range
# both are included
print('unofrom function-------')
val=random.uniform(10,20)
print(val)
#print(help(random.uniform))



#6) sample():->it will generate sample from the data
# it will give the output in the form of list
print('sample function-----')
li=['smruti','swagatika','jyoti','priti','raja']
var=random.sample(li,3)
print(var)
#print(help(random.sample))
data=random.sample(range(10000000), 60)
#print(data)



#7) choice() :-> It will generate only one data
print('choice function---')
l=[1,2,3,4,5,6]
val=random.choice(l)
print(val)

print('--')
l=range(10000)
v=random.choice(l)
print(v)

# QUESTIONS:--
 #find out the output?
print('q-1--')
li=[10,20,30,40,50,60]
data=random.sample(li,k=True+True*2)
print(len(data))
# ans is  3
print('--')
# here the output will be 20 (yes/No)
da=random.uniform(10,20)
print(da)
# ans is No