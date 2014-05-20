# The function is_anagram takes two strings as parameters, and 
# returns True if they are anagrams.
def is_anagram(str1, str2):
    list1 = sorted(str1)
    list2 = sorted(str2)
    if list1 == list2:
        return True
    else:
        return False

a = 'lure'
b = 'rule'
c = 'hello'
d = 'world'

print is_anagram(a, b)
print is_anagram(c, d)