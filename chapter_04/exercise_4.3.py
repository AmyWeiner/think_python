from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

# The function polygon takes a parameter named t, which is a turtle,
# a parameter named length, which is the length of a side, and a 
# a parameter n, which is the number of sides. It uses the turtle to 
# draw a polygon with n sides of length length.
def polygon(t, length, n):
    for i in range(n):
        degrees = 360.0 / n
        fd(t, length)
        lt(t, degrees)

polygon(bob, 30, 3)
polygon(bob, 40, 4)
polygon(bob, 50, 5)
polygon(bob, 60, 6)
polygon(bob, 70, 7)
