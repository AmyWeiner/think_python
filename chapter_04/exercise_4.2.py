from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

# The function square takes a parameter named t, which is a turtle,
# and a parameter named length, which is the length of a side. 
# It uses the turtle to draw a square with a side of length length.
def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

square(bob, 30)
square(bob, 60)
square(bob, 90)
square(bob, 120)