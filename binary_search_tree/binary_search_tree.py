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
            if not self.left == None:
                return False
            # otherwise, recursion on left node using target
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if the current node has a right node
        if self.right:
            # it has a larger number, so recursion
            return self.right.get_max()
        # otherwise this is max, so return the value
        else:
            return self.value

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
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
"""bst = BSTNode(1)

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
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
"""