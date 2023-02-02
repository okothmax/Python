# this method is similar to the binary_search technique but will return true or false instead of the values
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                # we create a new list through slice operation 
                return recursive_binary_search(list[midpoint + 1:], target)
                # the new list starts at midpoint+1 to the end and the target remains the same 
            else:
                return recursive_binary_search(list[:midpoint], target)

numbers = [3,34, 56, 67, 68] #the values have to be sorted
x = recursive_binary_search(numbers, 34)
print(x)