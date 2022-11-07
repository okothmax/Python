def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    Divide: Find the midpoint of the list and divide into sublist
    Conquer; Recursively sort the sublists created in previous step
    Combine: merge the sorted syblist created in previous step
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide unsorted list at the midpoint into sublist
    returns tw sublists - left and right
    Takes O(k log n) time
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    
    return (left, right)

def merge(left, right):
    """
    Merges two lists(arrays), sorting them in the process
    Returns a new merged list
    Takes n(log n) time"""
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    return l

myNumbers = [43, 87, 8, 90, 34, 100, 56, 5]
m = (merge_sort(myNumbers))
print(m)
