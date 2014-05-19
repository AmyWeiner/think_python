from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

# The function square takes a parameter named t, which is a turtle. 
# It uses the turtle to draw a square.
def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)

square(bob)