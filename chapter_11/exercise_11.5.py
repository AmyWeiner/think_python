def has_duplicates(list):
    dictionary = dict()
    for char in list:
        if char in dictionary:
            return True
        else:
            dictionary[char] = char
    return False
        


print has_duplicates([1, 2, 4, 2, 1])
print has_duplicates(['car', 'bus', 'train'])
print has_duplicates([1, 2, 3, 4, 5])
print has_duplicates(['car', 'car', 'van'])