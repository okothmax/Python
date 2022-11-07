def linear_search(list, target):
    """
    returns the index position of the target if found, else returns none
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
numbers = [2, 3, 4, 5, 6, 7, 8]
name = linear_search(numbers, 0)
print(name) 