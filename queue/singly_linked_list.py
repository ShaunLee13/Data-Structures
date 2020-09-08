class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # create a new node
        new_node = Node(value, None)
        # check if list has content:
        if not self.head:
            # if not, then our new_node will be set as the only item.
            self.head = new_node
            self.tail = new_node
        # otherwise:
        else:
            # our current tail will reach to the new node
            self.tail.set_next(new_node)
            # and we set the tail as the new node.
            self.tail = new_node

    def remove_head(self):
        # if there is nothing in the list:
        if not self.head:
            return None
        # else, if there's no items after head
        if not self.head.get_next():
            # make reference to show what is being removed
            head = self.head
            # delete the list reference 
            self.head = None
            # ensure that the tail has no reference as well
            self.tail = None
            # return the referenced value
            return head.get_value()
        # and if there is multiple items, get the value at the current head
        value = self.head.get_value()
        # and set head as the next node in the list
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        # if there is nothing in the list:
        if not self.head:
            return None
        # otherwise if the reference of head and tail is the same point:
        if self.head is self.tail:
            # get a reference where head is
            value = self.head.get_value()
            # and delete the reference for both
            self.head = None
            self.tail = None
            # return the previous reference
            return value
        # otherwise, set our current node at the head:
        current = self.head
        # as long as the next node in the list is not the tail
        while current.get_next() is not self.tail:
            # update our current node with the next reference
            current = current.get_next()
        # get a reference to the current tail before removing
        value = self.tail.get_value()
        # set our new tail to the value in current, which is one before current tail 
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False
    
        current = self.head
        # While there's a node not equal to None: 
        while current:
            # return True if current is equal to what we are searching for
            if current.get_value() == value:
                return True
            # otherwise we move to the next node by updating current
            current = current.get_next()
        # when there's no more nodes to access
        return False

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()
        current = self.head.get_next()

        # while our current node is not equal to None:
        while current:
            # compare max value to current to see if current is larger
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value