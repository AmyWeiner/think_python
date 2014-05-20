# The function first takes a string as a parameter, and returns the first
# character in the string.
def first(word):
    return word[0]

# The function last takes a string as a parameter, and returns the last
# character in the string.
def last(word):
    return word[-1]

# The function middle takes a string as a parameter, and returns the
# middle characters in the string.
def middle(word):
    return word[1:-1]

# The function is_palindrome takes a string as a parameter, and returns
# True if the string is a palindrome, and false otherwise.
def is_palindrome(word):
  """ for words of odd length"""
    if middle(word):
        if len(word) == 1:
            return True
        elif first(word) == last(word):
            word = word[1: -1]
            return is_palindrome(word)
        else:
            return False
    """ for words of even length"""
    if not middle(word):
        if len(word) == 0:
            return True
        elif first(word) == last(word):
            word = word[1: -1]
            return is_palindrome(word)
    else:
        return False

print is_palindrome('deified')
print is_palindrome('kayak')
print is_palindrome('noon')
print is_palindrome('abc')
print is_palindrome('I')
print is_palindrome('')