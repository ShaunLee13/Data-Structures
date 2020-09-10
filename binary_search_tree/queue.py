"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    # Determine the length of the queue
    def __len__(self):
        return self.size

    # Add a value to the end of the queue and increment size by 1
    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    # Remove the value at the 0 index and decrement size by 1
    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.pop(0)

# from singly_linked_list import LinkedList

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size

#     # Rather than append, we use the add_to_tail function.
#     def enqueue(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1

#     # Rather than popping an index, we can just use the remove_head to get the first one.
#     def dequeue(self):
#         if self.size == 0:
#             return None
#         self.size -= 1
#         return self.storage.remove_head()