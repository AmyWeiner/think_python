# The function square_root takes an integer, a, as a parameter,
# and returns an estimate of the square root of a.
def square_root(a):
    x = a / 2
    epsilon = 0.000001
    while True:
        print x
        y = (x + (a / x)) / 2
        if abs(y - x) < epsilon:
            break
        x = y

print square_root(25)