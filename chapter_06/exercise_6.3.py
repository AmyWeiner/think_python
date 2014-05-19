# The function is_between takes three integers, x, y, and z, as parameters,
# and returns True if the value of y falls between the values of x and z on a 
# number line, and false otherwise.
def is_between(x, y, z):
    if x <= y and y <= z:
        return True
    else:
        return False


print is_between(3, 4, 5)
print is_between(6, 10, 2)