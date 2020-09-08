"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{self.prev}, {self.value}, {self.next}'
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new node
        new_node = ListNode(value, None, None)
        # check if list has content:
        if not self.head:
            # if not, we will assign our previous head to current
            self.head.prev = self.head
            #and update our head and tail accordingly
            self.head = new_node
            self.tail = new_node
        # otherwise:
        else:
            current = self.head
            print(repr(current))
            # head's next will be set to the current head
            self.head.next = current
            # our head's previous will be updated by our current
            self.head.prev = new_node
            # and we set the head as the new node.
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # if there is nothing in the list:
        if not self.head:
            return None
        # else, if there's no items after head
        if not self.head.next:
            # make reference to show what is being removed
            head = self.head
            # delete the list reference 
            self.head = None
            # ensure that the tail has no reference as well
            self.tail = None
            # return the referenced value
            return head.get_value()
        # and if there is multiple items, get the value at the current head
        value = self.head
        # and set head as the next node in the list
        self.head = self.head.next
        return value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create a new node
        new_node = ListNode(value, None)
        # check if list has content:
        if not self.head:
            # if not, we will assign our previous head to current
            self.head.prev = self.head
            #and update our head and tail accordingly
            self.head = new_node
            self.tail = new_node
        # otherwise:
        else:
            # we will set our prev value as our current tail,
            self.tail.prev = self.tail
            # our current tail will connect to the new node,
            self.tail.next = new_node
            # and then we will set the tail as the new node.
            self.tail = new_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if there is nothing in the list:
        if not self.head:
            return None
        # otherwise if the reference of head and tail is the same point:
        if self.head is self.tail:
            # get a reference where head is
            value = self.head
            # and delete the reference for both
            self.head = None
            self.tail = None
            # return the previous reference
            return value
        prev = self.tail.prev
        # otherwise, get a reference to the current tail before removing
        value = self.tail.get_value()
        # and set our tail to our tail's prev reference
        self.tail = prev    
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass