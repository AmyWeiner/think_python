# The function chop takes a list, modifies it by removing the first and last 
# elements, and returns None. 
def chop(list):
    list.pop(0)
    list.pop(-1)

l = [1, 2, 3, 4, 5, 6]
chop(l)
print l