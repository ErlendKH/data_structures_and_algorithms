
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# A node:
# {
#     'value': 4,
#     'left': None,
#     'right': None
# }

class BinarySearchTree:

    # Something pointing to the first node, like head.
     # For a BST, you call it root instead.
    def __init__(self):
        self.root = None # Use insert later instead of setting it
        # on initialization.

    # Steps for inserting a node in a binary search tree:
    # create new_node
    # if root == None then root = new_node
    # temp = self.root
    # while loop
        # if new_node == temp return False (cannot have duplicates)
        # compare its value with the first node:
        # if < left else > right
        # check if the spot is free or not:
        # if None insert new_node else move to next
    # Compare temp with the new_node.

    # Note: Cannot have duplicates (same value).
    def insert(self, value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root

        while (True): # Using return to cancel the while.
            # Cannot have duplicate/equal values.
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                # If temp.left is not none, set it as the temp.
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                # 
                temp = temp.right
    
    def contains(self, value):

        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False # if temp is None, return false.

        # Trying it myself first.
        # Check if root is None.
        # If not, check if value is root.value.
        # Then, do a while? ...
        
        # Alternative way of doing it:

        if self.root is None:
            return False
        
        temp = self.root
        
        while(True):
            if value == temp.value:
                return True
            
            if value < temp.value:
                if temp.left is None:
                    return False
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    return False
                else:
                    temp = temp.right
    
    # 
    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
        # return current_node.value # testing

my_tree = BinarySearchTree()
# print(my_tree.root)

# 1: insert

# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# print(my_tree.root.value) # 2
# print(my_tree.root.left.value) # 1
# print(my_tree.root.right.value) # 3

# 2: contains

# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# print(my_tree.contains(4)) # False
# print(my_tree.contains(3)) # True
# print(my_tree.contains(-2)) # False

# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)

# print(my_tree.contains(27))
# print(my_tree.contains(17))

# 3: Minimum value

# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# print(my_tree.min_value()) # 1

# my_tree.insert(5)
# my_tree.insert(4)
# my_tree.insert(0)

# print(my_tree.min_value()) # 0

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.min_value_node(my_tree.root))
print(my_tree.min_value_node(my_tree.root.right))
