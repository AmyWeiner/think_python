# The function nested_sum takes a nested list of integers,
# and adds up the elements from all of the nested lists.
def nested_sum(list):
    total = 0
    for subl in list:
        total += sum(subl)
    return total

l = [[1, 4], [3, 6], [2, 7], [5, 9]]
print nested_sum(l)