
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# A node:
# {
#     'value': 4,
#     'next': None
# }

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    # Adding node to the (queue) line ...
    def enqueue(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            # Hm, okay, setting the new node as last's next
            self.last.next = new_node
            # Then, setting the new node as the last.
            self.last = new_node

            # So with queues, when you add a node, the last
            # one added should become the last node.

        self.length += 1
    
    def dequeue(self):

        if self.length == 0:
            return None
        
        temp = self.first

        # If just 1 item, just "emptying" it.
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            # So setting self's next as the new first.
            self.first = self.first.next
            # Disconnecting the previous first (temp).
            temp.next = None

        self.length -= 1
        return temp

# 1

# my_queue = Queue(4)
# my_queue.print_queue()

# 2: enqueue

# my_queue = Queue(1)
# my_queue.enqueue(2)

# my_queue.print_queue()
# # 1
# # 2

# 3: Dequeue

my_queue = Queue(1)
my_queue.enqueue(2)
# my_queue.print_queue()

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())


