from swampy.TurtleWorld import *
from math import pi
world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.1

# The function arc takes a turtle, t, a radius, r,  and and arc, angle as 
# parameters, and draws an approximate fraction of a circle, based on the
# the degrees of the arc. 
def arc(t, r, angle):
    length = 2 * pi * r
    degrees = angle / 100.0
    for i in range(100):
        fd(t, length)
        lt(t, degrees)
        

arc(bob, 0.25, 90)
