from queue import Queue
from stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.value}'

    # Insert the given value into the tree
    def insert(self, value):
        # check whether the value is >= self; if < go to elif
        if value >= self.value:
            # if self has no right node, create node using value
            if self.right == None:
                self.right = BSTNode(value)
            # otherwise, recursion on right
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the target value is equal to self.value, contains is True
        if target == self.value:
            return True
        # otherwise check if target is less than value; if greater, skip to next elif
        elif target < self.value:
            # if true, and if self has no left node, return false
            if not self.left:
                return False
            # otherwise, recursion on left node using target
            else:
                return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    # This method is recursive:
    def get_max(self):
        #check that there is a node:
        if not self:
            return None
        # if the current node has a right node
        if self.right:
            # it has a larger number, so recursion
            return self.right.get_max()
        # otherwise this is max, so return the value
        else:
            return self.value

    '''
    Iterable Alternative:
        # Return the maximum value found in the tree
    def get_max(self):
        # while the current node has a right node
        while self.right:
            # continue moving right
            self = self.right
        # otherwise this is max, so return the value
        else:
            return self.value
    '''

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on the current value
        fn(self.value)
        # if current node has a left node, recursion on it
        if self.left:
            self.left.for_each(fn)
        # once returned, do the same for right
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # access the leftmost node from this tree first
        if self.left:
            self.left.in_order_print()
        #print the current node once the method is back
        print(self.value)
        # then traverse down right path and continue until done
        if self.right:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # Create a new queue
        values = Queue()
        # Add our starting node to the queue
        values.enqueue(self)
        # As long as the queue is not empty:
        while values.size > 0:
            # dequeue the first node in values and print it
            self = values.dequeue()
            print(self.value)
            #if there is a left node, add it to the queue
            if self.left:
                values.enqueue(self.left)
            #if there's a right node, add it as well
            if self.right:
                values.enqueue(self.right)
            #this increases our values.size
            #continuing the loop until done

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        #instantiate a stack
        values = Stack()
        #push starting node
        values.push(self)
        #while stack is not empty:
        while values.size > 0:
            #pop the node
            #print node.value
            self = values.pop()
            print(self.value)
            #if node.left:
                #push left node
            if self.left:
                values.push(self.left)
            #if node.right:
                #push right node
            if self.right:
                values.push(self.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        # check that there is a value here
        if self:
            # as long as there is a node, print this nodes value
            # NOTE: This function essentially works the same as dft_print
            # just with recursion instead of iteration
            print(self.value)
            # if children nodes exist, call method on them
            if self.left:
                self.left.pre_order_dft()
            if self.right:
                self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        # check that there is a value here
        if self:
            # if children nodes exist, call method on them
            if self.left:
                self.left.post_order_dft()
            if self.right:
                self.right.post_order_dft()
            # after returning from subtrees, print this nodes value
            print(self.value)


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
