# The function histogram takes a string as a parameter, and returns
# a histogram of the characters in the string. 
def histogram(s):
    d = dict()
    for c in s:
            d[c] = d.get(c, 0) + 1
    return d

h = histogram('brontosaurus')
print h