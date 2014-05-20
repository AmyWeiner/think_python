# The function is_power takes two integer parameters, a and b, 
# and returns True is a is a power of b, and False, otherwise
def is_power(a, b):
    if a / b == 1:
        return True
    elif a % b == 0:
        a = a / b
        return is_power(a, b)
    else:
        return False

print is_power(27, 3)
print is_power(24, 6)
print is_power(64, 4)