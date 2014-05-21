# The function histogram takes a string as a parameter, and returns
# a histogram of the characters in the string. 
def histogram(s):
    d = dict()
    for c in s:
            d[c] = d.get(c, 0) + 1
    return d

# The function has_duplicates takes a list as a parameter, and returns 
# True if there is any element that appears more than once.
def has_duplicates(list):
    dictionary = histogram(list)
    for key in dictionary:
        if dictionary[key] > 1:
            return True
    return False


print has_duplicates([1, 2, 4, 2, 1])
print has_duplicates(['car', 'bus', 'train'])
print has_duplicates([1, 2, 3, 4, 5])
print has_duplicates(['car', 'car', 'van'])