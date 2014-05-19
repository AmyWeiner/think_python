from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

# Draws a square
for i in range(4):
    fd(bob, 100)
    lt(bob)

wait_for_user()
