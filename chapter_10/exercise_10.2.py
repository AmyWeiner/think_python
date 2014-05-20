# The function capitalize_all takes a list of strings, and returns a new
# list that contains capitalized strings.
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

# The function capitalize_nested takes a nested list of strings, and 
# returns a new nested list with all strings capitalized.
def capitalize_nested(list):
    result = []
    for subl in list:
        temp = capitalize_all(subl)
        result.append(temp)

    return result


l = [['cat', 'dog'], ['bird', 'bat'], ['mouse', 'hog'], ['horse', 'rat']]
print capitalize_nested(l)