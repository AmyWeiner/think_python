from swampy.TurtleWorld import *
from math import pi
world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.1

# The function polygon takes a parameter named t, which is a turtle,
# a parameter named length, which is the length of a side, and a 
# a parameter n, which is the number of sides. It uses the turtle to 
# draw a polygon with n sides of length length.
def polygon(t, length, n):
    for i in range(n):
        degrees = 360.0 / n
        fd(t, length)
        lt(t, degrees)


# The function circle that takes a turtle, t, and radius, r, as parameters and 
# draws an approximate circle by invoking polygon with an appropriate length 
# and number of sides.
def circle(t, r):
    length = 2 * pi * r
    polygon(t, length, 100)

circle(bob, 0.5)
circle(bob, 0.75)
circle(bob, 1)
