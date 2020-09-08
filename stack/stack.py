"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     # equivalent of doing len()
#     def __len__(self):
#         return self.size

#     # increment the size counter by one and append value onto the end of storage
#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)

#     # decrement the size counter by one and pop value from the end
#     def pop(self):
#         # ensure that storage has contents first
#         if self.size == 0:
#             return None
#         self.size -= 1
#         return self.storage.pop()


from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    # add to tail method replaces append
    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    #remove tail replaces pop method
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()