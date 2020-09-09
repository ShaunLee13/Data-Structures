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
        # create a new node and increase length
        new_node = ListNode(value, None, None)
        self.length += 1

        # check if list has content:
        if not self.head and not self.tail:
            # if not, set head and tail to our new node
            self.head = new_node
            self.tail = new_node
        # otherwise:
        else:
            # we'll point our next pointer at the current head
            # set our prev pointer to the new node
            # and set our head as the new node
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # create a variable to store the value held at head
        value = self.head.value
        # run the delete method created to delete
        self.delete(self.head)
        # return the value stored in variable
        return value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create a new node and increase length
        new_node = ListNode(value, None, None)
        self.length += 1
        # check if list has content:
        if not self.head and not self.tail:
            # if not, set head and tail to our new node
            self.head = new_node
            self.tail = new_node
        # otherwise:
        else:
            # we will set our prev value as our current tail,
            # our current tail will connect to the new node,
            # and then we will set the tail as the new node.
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # create a variable to store the value held at tail
        value = self.tail.value
        # run the delete method created to delete
        self.delete(self.tail)
        # return the value stored in variable
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # if the node is already at the head, do nothing
        if node is self.head:
            return
        # otherwise create a variable to store the value of the node
        value = node.value

        # if that node is the tail value
        if node is self.tail:
            # remove it from the tail
            self.remove_from_tail()
        #otherwise
        else:
            # delete the node and dec length
            node.delete()
            self.length -= 1
        # create a new node at head with the variable
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return

        value = node.value

        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # Check that there's no content
        if not self.head and not self.tail:
            return
        
        # if content, dec length by 1
        self.length -= 1

        # if there's only one item in the list,
        # clear it from the list by setting head and tail to none
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        # otherwise, if the head is the node we want,
        # set the head to the next node in chain before deletion
        elif self.head == node:
            self.head = node.next
            node.delete()

        # otherwise, if the tail is the node we want,
        # set the tail to the prev node in chain before deletion
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        
        # otherwise you can just delete the node
        else:
            node.delete()

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # if there's no content, return None
        if not self.head:
            return None
        # otherwise, set 2 variables. one for value comparison, one for nodes
        max_val = self.head.value
        current_node = self.head
        # as long as there are nodes in the list:
        while current_node:
            # compare the previous max value to the value at the current node
            # and if it is higher, then overwrite max_val
            if current_node.value > max_val:
                max_val = current_node.value

            # move to the next node
            current_node = current_node.next
        
        return max_val