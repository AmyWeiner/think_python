# The function histogram takes a string as a parameter, and returns
# a histogram of the characters in the string. 
def histogram(s):
    d = dict()
    for c in s:
            d[c] = d.get(c, 0) + 1
    return d

h = histogram('committee')

# The function reverse_lookup takes a dictionary and a value as parameters,
# and returns a list of all keys that map to the given value, or an empty 
# list if there are none.
def reverse_lookup(dictionary, value):
    result = []
    for key in dictionary:
        if dictionary[key] == value:
            result.append(key)
    return result

print reverse_lookup(h, 2)