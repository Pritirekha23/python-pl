# Nested of function or inner function
   # If a function is present inside another function ,then that function is called nested function.

print('Nested function')
def outer_fun():
   print("I am inside outer fun")

   def inner_fun():
      print("I am inside inner fun")
   inner_fun()

outer_fun()

print('Nested function ex---2')
def outer_fun():
   print("I am inside outer fun")

   def inner_fun():
      print("I am inside inner fun")
   
   
outer_fun()
#inner_fun() NameError: name 'inner_fun' is not defined. Did you mean: 'outer_fun'?  
# we cant call a inner function outside of the outer function. we can call the inner function only inside the outer function. 