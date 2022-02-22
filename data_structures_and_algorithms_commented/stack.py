
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# A node:
# {
#     'value': 4,
#     'next': None
# }

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # 
    def push(self, value):
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
        else:
            # First, set new node's next to the current top
            new_node.next = self.top
            # Then, set the new node as the new top.
            self.top = new_node
        
        self.height += 1

    # Removes the top node
    # Returns the popped node
    def pop(self):
        if self.height == 0:
            return None
        
        # current top assigned to temp
        temp = self.top
        # setting the top's next as the new top
        self.top = self.top.next
        # Disconnecting temp from the stack
        temp.next = None

        self.height -= 1
        return temp
        
# 1

# my_stack = Stack(4)
# my_stack.print_stack()

# 2: push

# my_stack = Stack(2)
# my_stack.push(1)

# my_stack.print_stack()
# # 1
# # 2

# 3: pop

my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

print(my_stack.pop(), '\n') # removed 11 -- The last one pushed.

my_stack.print_stack()
# 3
# 23
# 7
