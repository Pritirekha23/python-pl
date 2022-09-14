# Numeric functions in math module
#ceil()-it means the smallest integral value greater than the number
#floor()-it means the greatest integral value smaller than the number
#factorial()-it gives the factorial of a number
#gcd()-it is used to find the greatest common divisor of two numbers passed as the arguments
#fabs()-it returns the absolute value of the number
#exp()-it is used to calculate the power of e i.e e^y or we can say exponential of y
#pow()-it first converts its arguments into float and then computes the power. function computes x**y 
  #log--
#log()-it return the logarithmic value of a with base b.If the base is not given,the computed valuer is the natural log.
#log2(a)-it computes the value of log a with base 2 .
#log10(a)-it computes the value of log a with base 10.
#sqrt()-it return the square root of a number

#Trigonmetric & angular function:--
#sin(),cos(),tan() - it returns the sine,cosine and tangent of value passed as the argument . The value passed in this should be in radians.

# converting values from degrees to radians and vice versa

  # degrees()-it is used to convert argument value from radians to degrees.
  # radians()-it is used to convert argument value from  degrees to radians .


# SPECIAL functions
  #gamma()-it is used to return the gamma value of the argument.



import math
print(math.ceil(3.2))
print(math.floor(3.2))
print("gcd")
print(math.gcd(20,3))
print(math.fabs(-10))
print(math.exp(-3))
print(math.pow(2,3))
print(math.log(2,4))
print(math.log2(16))
print(math.log10(1000))
print(math.sqrt(2))

print('trigonmetric')
a=math.pi/6
print(math.sin(a))
print(math.cos(a))
print(math.tan(a))
print('---')
print(math.degrees(a))
print(math.radians(a))

print(math.gamma((6)))

# check  if the value is infinity or nan
  # isinf()- it is used to check whether the value is infinity or not

  # isnan()- it  returns true if the number is "NaN" else return false.

print('----')
print(math.isinf(math.pi))
print(-math.isinf(math.e))

print(math.isnan(math.pi))
print(math.isnan(math.e))

# hypot()-it return Eucliderm norm root of (x*x+y*y)

print(math.hypot(3,4))















