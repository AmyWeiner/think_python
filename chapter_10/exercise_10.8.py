# The function has_duplicates takes a list as a parameter, and returns 
# True if there is any element that appears more than once.
def has_duplicates(list):
    for item in list:
        if list.count(item) > 1:
            return True
        else:
            return False

print has_duplicates([1, 2, 4, 2, 1])
print has_duplicates(['car', 'bus', 'train'])
print has_duplicates([1, 2, 3, 4, 5])
print has_duplicates(['car', 'car', 'van'])