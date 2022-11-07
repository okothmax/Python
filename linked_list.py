# creating a class to represent a node
class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node in the list
    """
    data = None # holds the data we're storing
    next_node = None # points to the next data in the list
    # we add a contructor to make the class easy to create
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>" % self.data
 
 # nodes are the building block for a singly linked list and now that we have a node we can create a singly linked list

class LinkedList:
    head = None
    """
    singly linked list
    """
    def __init__(self):
        self.head = None   # By having this we can remove line 18
     
    def is_empty(self):
        return self.head == None   # Checking to see if the list is empty
    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

 # how to add some data into a linked list
 # we define a method called add

    def add(self, data):
        """
        Adds a new node at the head of the list 
        Take O(1) constant time"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

 # To search move a value in our list
 # To return either the node of the value if found or returns None

    def search(self,key):
        """
        Search for the first node that contains data that matches the key
        Returns None if not found
        Takes O(n) linear time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return 
        
 # inserts and deletes at specific loactions 

    def insert(self, data, index):
        """
        inserts a new node containing data at a index position 
        insertion takes O(1) contant time but finding the node t the insertion point takes O(n) linear time 
        therefore it takes an overall O(n) linear time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = Node.next_node
                position -= 1

                prev_node = current
                next_node = current.next_node

                prev_node.next_node = new
                new.next_node = next_node 

# removing a node 

    def remove(self, key):
        """
        Removes node that contains data matching the key
        Returns the node or none if not found 
        takes O(n) linear time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        """
        return a string representation of the list
        Takes O(n) linear time"""

        nodes =[]
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(nodes)

