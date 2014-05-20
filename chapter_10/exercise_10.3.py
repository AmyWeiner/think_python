# The function middle takes a list, and returns a new list 
# that contains all but the first and last elements.
def middle(list):
    result = list[1:-1]
    return result


l = [1, 2, 3, 4, 5, 6]
print middle(l)