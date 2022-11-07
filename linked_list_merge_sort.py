from platform import node
from re import L
from linked_list import LinkedList
# we then test whether the import runs correctly
# l = LinkedList()
# l.add(3)
# l.add(2)
# print(l)

def merge_sort(linked_list):
    """
    Sorts a linked list in ascednding order
    Recursively dived the linked list into sublist containing a single node
    repeatedly merge the sublist to produce sublists until one remains
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted linked list into sublists
    """
    if linked_list == None or linked_list.head == None :
        left_half = linked_list
        right_half = None

        return left_half, right_half

    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """
    merges two linked list, sorting by data of nodes
    returnd a new merged list
    """
    # create a new linked list that contains nodes from 
    # merging the left and right 
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # set current to the head of the list
    current = merged.head

    # obtain head for left and right linked lists
    left_head = left.head
    right_head = right.head

    # interate over left and riifgt until we reach the tail node of either
    while left_head or right_head:
        # if the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # call next on right to set loop condition to false
            right_head = right_head.next_node
        # if the head node of right is None, we're past the tail
        # add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            # not at either tail node
            # obtain node data to perform comparison operation
            left_data = left_head.data
            right_data = right_head.data
            # if data on the left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to the next node
                left_head = left_head.next_node
            # if data on right is greater than data on left 
            else:
                 current.next_node = right_head
                 # move right head to the next node
                 right_head = right_head.next_node
        # move current to the next node 
        current = current.next_node 
    # discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()
l.add(2)
l.add(0)
l.add(1.5)
l.add(56)
l.add(34)
print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)

