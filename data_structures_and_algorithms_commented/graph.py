
#    		A	
#   E				B
#    	D		C	

# {
#     'A': ['B', 'E'],
#     'B': ['A', 'C'],
#     'C': ['B', 'D'],
#     'D': ['C', 'E'],
#     'E': ['D', 'A']
# }

# {
#     'A': []
# }

class Graph:
    def __init__(self):
        self.adj_list = {} # Creating an empty dictionary.

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        # Only add if it doesn't already exist (checking the keys)
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):

        # Hm... Error checking first -- if both exists
        # (returns true in the if statement)
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():

            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):

        # One problem -- Trying to remove an edge that doesn't exist
        # in the adjacency list.

        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try: # detects errors if any.
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
            except ValueError:
                pass # ignoring the error and move on
            return True
        return False

    # Efficiency: So when removing a vertex, first, remove all
    # edges between it and other vertices. Then, you can remove it.
    def remove_vertex(self, vertex):
        
        # First, checking if the vertex exists in the keys:
        if vertex in self.adj_list.keys():
            # Then, looping between the vertices connected
            # to the vertex we wish to remove:
            for other_vertex in self.adj_list[vertex]:
                # Remove the vertex from the other vertices
                # (in order to remove edges with it).
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
    
        return False # If the vertex doesn't exist.
    
my_graph = Graph()

# my_graph.add_vertex('A')
# my_graph.print_graph() # A : []

# 1: add edge

# my_graph.add_vertex(1)
# my_graph.add_vertex(2)

# my_graph.add_edge(1, 2)
# my_graph.print_graph()

# 2: remove edge

# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')

# my_graph.add_edge('A', 'B')
# my_graph.add_edge('B', 'C')
# my_graph.add_edge('C', 'A')

# my_graph.remove_edge('A', 'D')

# my_graph.print_graph()

# 3: Remove vertex

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

# my_graph.print_graph()

my_graph.remove_vertex('D')

my_graph.print_graph()
