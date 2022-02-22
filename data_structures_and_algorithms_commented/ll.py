
# self --> to specific instance.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# A node is:
# {
#     "value": 4,
#     "next": None
# }

class LinkedList:
    # Meaning -- Method inside of a class instead of being
    # a standalone function.
    def __init__(self, value):
        # create new Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # prints the nodes. Not really a list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # create new Node
        # add Node to end
        new_node = Node(value)

        # If the list is empty:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True # For eventually returning a bool value.

    def prepend(self, value):
        # create new Node
        # add Node to beginning
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # Sets the current head (self.head)
            # to be the prepending node's next.
            new_node.next = self.head
            # Sets prepending node to be the new head.
            self.head = new_node 
        self.length += 1
        return True

    # Insert -- So adding a new node ... Anywhere.
    def insert(self, index, value):
        # create new Node
        # insert Node

        # Note 1: return (early, not keep running code)
        # Note 2: self (running on this particular linked list)

        # First, need to check for a valid index again...
        if index < 0 or index > self.length:
            return False
        
        # Adding to the beginning.
        if index == 0:
            return self.prepend(value)
            # We use prepend and append in this function,
            # which is why we have them return a bool value.

        # OK, so if the index is equal to the length of the
        # linked list, can just add it using append.
        # Adding to the end.
        if index == self.length:
            return self.append(value)
        
        # For values in the middle, need to use a temp variable again.
        new_node = Node(value)
        temp = self.get(index - 1)

        # Ok, for making the new node point to the next node
        # of the temp node (which is index - 1).
        new_node.next = temp.next 
        # And now, updating temp's next node to be the new node.
        temp.next = new_node

        self.length += 1
        return True

    def remove(self, index):
        # First, check index
        if index < 0 or index >= self.length:
            return None
        
        # Remove first node.
        if index == 0:
            return self.pop_first()
        
        # Remove the last node.
        if index == self.length - 1:
            return self.pop()

        # Removing a node somewhere in the middle.

        # Hm, we'll need a prev and temp node.
        # A prev to point to the next node.
        prev = self.get(index - 1)
        temp = prev.next # So temp is the next node of prev.

        # Make prev point to the next node of temp:
        prev.next = temp.next
        temp.next = None # Removing temp out of the list.
        self.length -= 1

        return temp # Returning the removed node.
        # return temp.value # testing

    # Pop -- Removing the last node
    def pop(self):

        # If no items to pop/remove, just return none.
        if self.length == 0:
            return None
        # Oh, okay, don't need else: here. It returns early.

        # temp and pre start at the head.
        temp = self.head
        pre = self.head

        # Runs while temp.next is true.
        # So it'll be false when it reaches None?
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre # Setting the new tail node.
        self.tail.next = None # Breaking off previously final node.
        self.length -= 1 # One less node.

        # If the length is 0 AFTER the decrementation:
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp # return a node here (temp)

        # Hm, okay. So returning temp... If the length was 1,
        # it will return the previous self.head node.

        # If the length is 0, the lines at the top:
        # if self.length == 0
        #   return None
        # will already have triggered.

        # return temp.value # For debugging.

    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head # The first node.
        # Aha... Sets the head's next node as the new head.
        self.head = self.head.next

        temp.next = None # 
        self.length -= 1

        # If the length was 1 and is now 0:
        if self.length == 0:
            self.tail = None
        return temp
        # return temp.value # testing
    
    def get(self, index):
        # First, test for a valid index to avoid errors.
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        # If you don't use i, replace it with an underscore.
        for _ in range(index):
            temp = temp.next
        # Hold on... What did the loop above do? Oh, okay, 
        # it just traverses through the list to the last index.
        return temp
        # return temp.value # testing

    # set is a key value, so got to call it something else,
    # like set_value.
    def set_value(self, index, value):

        # I suppose we need to check for a valid index again.
        # if index < 0 or index >= self.length:
        #     return None 

        # Ah, can check if it's valid here too.
        temp = self.get(index)
        # If temp is not null ... The "if temp:" will either
        # return a node or None/null.
        if temp: 
            temp.value = value
            return True
        return False

    # So the idea is to switch the head and tail, and then
    # reverse the pointers of all the nodes.
    def reverse(self):
        # temp equals to head.
        # head equals to tail.
        # tail equal to temp.
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # before
        # temp
        # after
        # Hm. So these nodes need to be in a particular order.

        # temp is the head, so
        # after is the temp's (head's) next node.
        after = temp.next
        before = None # before's first value.

        # Example: linked list of 1, 2, 3, 4.
        # temp = 1
        # self.head = 4
        # self.tail = 1
        # after = 2
        # before = None

        for _ in range(self.length): # from index 0 to length-1.

            after = temp.next # after is temp's next node.
            temp.next = before # reverses temp's next.
            # Moving before to temp.
            before = temp
            # Moving temp to after.
            temp = after

            # Continuing with the example -- index 0:
            # after = 2 # Sets after foward one node of temp.
            # temp.next = None # Sets temp's next node to None.
            # before = 1 # Here, moves before forward one node.
            # temp = 2 # Moves temp forward one node.

            # index 1:
            # after = 3
            # temp.next = 1
            # before = 2
            # temp = 3

            # index 2:
            # after = 4
            # temp.next = 2
            # before = 3
            # temp = 4

            # index 3:
            # after = None
            # temp.next = 3
            # before = 4
            # temp = None

            # 

# 1

# Creating a linked list of the LinkedList class.
# my_linked_list = LinkedList(4)
# print(my_linked_list.head.value) # 4
# my_linked_list.print_list() # 4

# 2

# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# # my_linked_list.print_list()
# # # 1
# # # 2

# 3: Pop

# print(my_linked_list.pop())
# # print(my_linked_list.length)
# print(my_linked_list.pop())
# # print(my_linked_list.length)
# print(my_linked_list.pop())
# # print(my_linked_list.length)

# 4: Prepend

# my_linked_list = LinkedList(2)
# my_linked_list.append(3)
# # my_linked_list.print_list()
# my_linked_list.prepend(1)
# my_linked_list.print_list()
# # 1
# # 2
# # 3

# 5: Pop first

# my_linked_list = LinkedList(2)
# my_linked_list.append(1)
# # my_linked_list.print_list()
# print(my_linked_list.pop_first()) #
# print(my_linked_list.pop_first()) # 
# print(my_linked_list.pop_first()) # None

# 6: Get

# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# # print(my_linked_list.length)
# # print(my_linked_list.print_list())
# # # Hm, why does it return a None at the end of print_list?
# # Oh, okay, because it just prints node.next.
# # When the next value is None, it prints out that too...
# print(my_linked_list.get(2))

# 7: set_value

# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)
# # OK, so index 1 points to the second node.
# my_linked_list.set_value(0, 55)
# my_linked_list.set_value(1, 4)
# my_linked_list.print_list()

# 8: insert

# my_linked_list = LinkedList(0)
# my_linked_list.append(2)
# # my_linked_list.print_list()
# # OK, so it inserted 1 after 0 and before 2.
# # 0 at index 0 points to 1 and have the new node 1 point to 2.
# my_linked_list.insert(1,1)
# my_linked_list.print_list()
# # 0
# # 1
# # 2

# 9: remove

# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)
# # my_linked_list.print_list()

# print(my_linked_list.remove(2), '\n')
# my_linked_list.print_list()

# 10: reverse

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
# my_linked_list.print_list()

my_linked_list.reverse()
my_linked_list.print_list()
# 4
# 3
# 2
# 1