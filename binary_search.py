def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2 # the // represent a floor which rounds off to the nearest whole number
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1 
    return None

numbers = [3,34, 56, 67, 68] #the vales have to be sorted
x = binary_search(numbers, 68)
print(x)