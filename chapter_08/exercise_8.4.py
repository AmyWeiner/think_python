# The function count takes a string and a letter as arguments, and returns
# the number of times that the letter occurrs in the string.
def count(word, target):
    counter = 0
    for letter in word:
        if letter == target:
            counter += 1
    return counter

print count('banana', 'n')
print count('Mississippi', 'i')