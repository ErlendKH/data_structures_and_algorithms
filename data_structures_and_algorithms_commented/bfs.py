
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    # Something pointing to the first node, like head.
     # For a BST, you call it root instead.
    def __init__(self):
        self.root = None # Use insert later instead of setting it
        # on initialization.

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
    
    # 
    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

###

    # Breadth First Search is a method within a 
    # binary search tree.
    def BFS(self):
        current_node = self.root
        # using what's most familiar here -> lists
        queue = [] 
        results = []

        queue.append(current_node)

        while len(queue) > 0:
            # current node is the node we remove from the queue
            current_node = queue.pop(0)
            results.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return results

    def dfs_pre_order(self):
        results = []

        # recursive -- uses call stacks to traverse the 
        # binary search tree.
        def traverse(current_node):
            # 
            results.append(current_node.value)

            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        # Calls the inner traverse function.
        traverse(self.root)
        return results # Returns the traversed list.

        # Explanation with the following example:
        # First, it will append 47.
        # Then, it will find a node on the left (21).
        # Then, it will find another node on the left (18).
        # Since 18 doesn't have any children, it will be removed
        # from the stack.
        # Then it checks 21, which has a child to the right (27).
        # 27 has no children so it'll be removed from the stack.
        # 21 is done so will be removed from the stack.
        # 47 has a child on the right (76). ...
    
    # Will add the value before it's removed from the stack.
    # This function will add values beginning from the
    # bottom-end and then go up the current branch,
    # and do each branch to the right.
    # The root node will be added last.
    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            # Adding the value before being taken off the stack
            results.append(current_node.value)
        
        traverse(self.root)
        return results
    
    # So in order is going to add the value after going left
    # and before going right.
    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)

            # Adding value before going right.
            results.append(current_node.value)

            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root) # Calling the inner traverse method.
        return results

#			    47
#        21				76
#    18		27		52		82

my_tree = BinarySearchTree()

# 1: Breadth first search

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# print(my_tree.BFS()) # [47, 21, 76, 18, 27, 52, 82]

# 2: Depth first search - PreOrder

print(my_tree.dfs_pre_order()) # [47, 21, 18, 27, 76, 52, 82]

# 3: Depth first search - PostOrder

print(my_tree.dfs_post_order()) # [18, 27, 21, 52, 82, 76, 47]

# 4: Depth first search - InOrder

print(my_tree.dfs_in_order()) # [18, 21, 27, 47, 52, 76, 82]