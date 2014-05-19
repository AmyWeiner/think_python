from math import *

# The function hypotenuse takes two integers, a and b, as
# arguments, and returns the length of the hypotenuse
# of a right triangle given the lengths of the two legs a and b.
def hypotenuse(a, b):
    c_squared = a**2 + b**2
    c = sqrt(c_squared)
    return c

print hypotenuse(3, 4)