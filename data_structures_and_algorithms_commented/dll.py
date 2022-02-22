
class Node:
    # Hm... Does it have to be called exactly __init__?
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# A node:
# {
#     'value': 7,
#     'next': None,
#     'prev': None
# }

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Adds a node to the end
    def append(self, value):
        new_node = Node(value)

        #
        if self.head is None: # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            # Hm, okay, so append is adding to the end.
            # Adding new_node to the end of tail.next.
            self.tail.next = new_node
            # Adding pointer from new_node back to the tail.
            new_node.prev = self.tail
            # And finally, setting the new_node as the new tail.
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        # temp is the current tail (which we will break off)
        # set tail.prev as the new tail.
        # tail.next = None
        # temp.prev = None

        if self.length == 0:
            return None
        
        temp = self.tail # Setting temp here as the tail.
        if self.length == 1:
            self.head = None
            self.tail = None
        else: # 2 or more items.
            # Setting the new tail as the old tail's prev
            self.tail = self.tail.prev
            # Setting new tail's next to None to break pointer forward.
            self.tail.next = None
            # Setting temp.prev (old tail's prev) to None to break pointer back.
            temp.prev = None
        self.length -= 1
        return temp
        # return temp.value # testing

        # temp = self.tail # current tail
        # self.tail = self.tail.prev # sets tail to its prev.
        # self.tail.next = None # Breaks new tail's next.
        # temp.prev = None # Breaks old tail's prev connection.
        # self.length -= 1

        # # If length was 1 and is now 0:
        # if self.length == 0:
        #     self.head = None
        #     self.tail = None
        # return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node -> current head
            new_node.next = self.head
            # and pointer from head to the new_node <-
            self.head.prev = new_node
            # Finally, set the new node as the new head.
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):

        if self.length == 0:
            return None
        
        temp = self.head # Does this in order to return the popped node.

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # Sets the head's next as the new head
            self.head = self.head.next
            # Removes the head's prev node.
            self.head.prev = None
            # Finally, removes the old head's next.
            temp.next = None
        
        self.length -= 1
        return temp
        # return temp.value # testing

    def get(self, index):

        # First, check if the index is valid:
        if index < 0 or index >= self.length:
            return None

        temp = self.head

        # Optimization.
        # If the index is within the first half
        # of the dll, do a for loop (incrementing forward).
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else: 
            # If the index is within the second half of the dll,
            # start at the tail and increment backwards.
            temp = self.tail
            # Backwards loop:
            # Begin at index self.length-1. Incr. by -1 for
            # index
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
                
        return temp
        # return temp.value # testing

    def set_value(self, index, value):
        temp = self.get(index)
        # So, if temp is a valid node (not null/None),
        # the code will execute and return True.
        if temp:
            temp.value = value
            return True
        # If the get(index) doesn't return a valid node,
        # return false.
        return False
    
    def insert(self, index, value):

        # If index is not valid.
        if index < 0 or index > self.length:
            return False
        
        # If inserting at the start, just use prepend.
        if index == 0:
            return self.prepend(value)

        # If inserting at the end (last index + 1), just append...
        if index == self.length:
            return self.append(value)

        # In the middle.
        # before
        # after
        new_node = Node(value)
        # before is the node before the index we want to add
        # the new node.
        before = self.get(index-1)
        # after is the node to the right of before.
        after = before.next

        # So, placing the new node in between before and after:
        new_node.prev = before
        new_node.next = after

        # Connecting before to the new node
        before.next = new_node
        # Connecting after to the new node
        after.prev = new_node

        self.length += 1
        return True
    
    def remove(self, index):

        # index validation
        if index < 0 or index >= self.length:
            return None

        # if the index is 0
        if index == 0:
            return self.pop_first()

        # If it's the last index
        if index == self.length - 1:
            return self.pop()

        # before
        # temp
        # after

        temp = self.get(index)

        # Oh, okay. The next two lines connect the node before
        # temp and the node after with each other.

        # 
        temp.next.prev = temp.prev
        # 
        temp.prev.next = temp.next
        # The two following lines disconnect temp from the dll.
        temp.prev = None
        temp.next = None

        self.length -= 1
        return temp
        # return temp.value # testing
    
# 1

# my_doubly_linked_list = DoublyLinkedList(7)
# my_doubly_linked_list.print_list()

# 2: append

# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(2)

# my_doubly_linked_list.print_list()

# 3: pop

# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(2)
# # my_doubly_linked_list.print_list()

# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())

# 4: prepend

# my_doubly_linked_list = DoublyLinkedList(2)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.prepend(1)
# my_doubly_linked_list.print_list()

# 5: pop first

# my_doubly_linked_list = DoublyLinkedList(2)
# my_doubly_linked_list.append(1)
# # my_doubly_linked_list.print_list()
# print(my_doubly_linked_list.pop_first())
# print(my_doubly_linked_list.pop_first())
# print(my_doubly_linked_list.pop_first())

# 6: get

# my_doubly_linked_list = DoublyLinkedList(0)
# my_doubly_linked_list.append(1)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(3)
# # my_doubly_linked_list.print_list()
# print(my_doubly_linked_list.get(1))
# print(my_doubly_linked_list.get(2))

# 7: set

# my_doubly_linked_list = DoublyLinkedList(11)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.append(23)
# my_doubly_linked_list.append(7)

# my_doubly_linked_list.set_value(1, 4)

# my_doubly_linked_list.print_list()

# 8: insert

# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(3)

# my_doubly_linked_list.insert(1, 2)

# my_doubly_linked_list.print_list()
# # 1
# # 2
# # 3

# 9: remove

my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)

print(my_doubly_linked_list.remove(1), '\n')

my_doubly_linked_list.print_list()
# 0
# 2