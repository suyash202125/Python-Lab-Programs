# Design a "Graph" class that represent a Graph
# with edges as {Node1: (Node2, Weight1), Node2: (Node3, Weight2)}
class Graph:
    def __init__(self, no_of_nodes):
        # Data members
        self.No_of_node = no_of_nodes
        self.graph = dict()

    #adding edges with nodes using dictionary
    def add_edge(self, node1, node2, weight=1):
        if node1 in self.graph.keys():
            newval = (self.graph[node1],(node2,weight))
            self.graph[node1] = newval
        else:
            self.graph[node1] = (node2,weight)
    
    #printing graph
    def printGraph(self):
        print(self.graph)

#DRIVER CODE
g = Graph(5)
g.add_edge(1, 2, 7)
g.add_edge(2, 3, 1)
g.add_edge(3, 4, 3)
g.add_edge(4, 1, 5)
g.add_edge(2, 4, 6)
g.add_edge(3, 5, 2)
g.add_edge(5, 2, 4)
g.printGraph()