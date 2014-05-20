# The function cumulative_sum takes a list of numbers , and 
# returns the cumulative sum; that is, a new list where the ith 
# element is the sum of the first i + 1 elements from the original list. 
def cumulative_sum(list):
    result = []
    sum = 0
    for i in list:
        sum += i
        result.append(sum)  
    return result


items = [1, 2, 3]
print cumulative_sum(items)