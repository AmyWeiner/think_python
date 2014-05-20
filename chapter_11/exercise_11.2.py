# The function histogram takes a string as a parameter, and returns
# a histogram of the characters in the string. 
def histogram(s):
    d = dict()
    for c in s:
            d[c] = d.get(c, 0) + 1
    return d

h = histogram('brontosaurus')

# The function print_histogram takes a histogram as a parameter, and 
# prints, in alphabetical order, the keys and their values. 
def print_histogram(hist):
    result = []
    for char in hist:
        result.append(char)
    result.sort()
    for char in result:
        print char, hist[char]

print_histogram(h)
