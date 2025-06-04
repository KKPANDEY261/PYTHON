import math
# math.ceil()
#Round the decimal number up to the nearest larger integer.

print(math.ceil(4.3))  # Output: 5
print(math.ceil(-2.7)) # Output: -2

#math floor
#Rounds down a decimal number to the nearest smaller integer.

print(math.floor(4.9))  # Output: 4
print(math.floor(-2.3)) # Output: -3

#math fabs()
#Returns the absolute value of a number.

print(math.fabs(-7.25))  # Output: 7.25

#math.sqrt()
#Finds the square root of a number.

print(math.sqrt(25))  # Output: 5.0

#math.pow(x, y)
#Calculates x raised to the power of y.

print(math.pow(2, 3))  # Output: 8.0

#math.factorial(x)
#Calculates the factorial of a number.

print(math.factorial(5))  # Output: 120 (5! = 5×4×3×2×1)

#math.pi
#Value of π (≈ 3.141592653589793)

print(math.pi)  # Output: 3.141592653589793

#math.isclose(a, b)
#Checks whether two numbers are approximately equal.

print(math.isclose(1.0, 1.000000))  # Output: True

#math.remainder(x, y)
#Checks the remainder of x/y

print(math.remainder(10, 3))  # Output: 1.0

#math.e        
# (Euler's Constant)   value=2.718281828459045

print(math.e)  # Output: 2.718281828459045 (e^1)

#math.exp
#(Exponential)
#Calculates e raised to the power x 


print(math.exp(2))  # Output: 7.3890560989306495 (e^1)


#math.fabs()     
# return positive float
import math
print(math.fabs(-7.25))  # Output: 7.25
print(math.fabs(-7))          # Output: 7.0

#math.abs() 
# maintain the data type and return positive value

print(abs(-7.25))       # Output: 7.25 
print(abs(-7))          # Output: 7 
