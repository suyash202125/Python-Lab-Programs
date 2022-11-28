# Below is a "Graph" class that represent a Graph
# with directed edges as {Node1: [connected nodes],
# Node2: [connected nodes]}
class Graph:
    '''Graph class has three function that performs:
       1. initialization of number of nodes
       2. represents added directed edges in a dictionary 
       with connected nodes.
       3. returns the directed graph'''
    def __init__(self, no_of_nodes):
        # Data members
        self.No_of_node = no_of_nodes
        self.graph = dict()

    #adding edges with nodes using dictionary
    def add_edge(self, node1, node2):
        '''adds edges and represents in the form 
            of a dictionary'''
        if node1 in self.graph.keys():
            newval = self.graph[node1]
            newval.append(node2)
            self.graph[node1] = newval
        else:
            self.graph[node1] = [node2]
    
    #return graph
    def getGraph(self):
        '''returns the graph'''
        return self.graph


class GraphTraversal:
    '''GraphTraversal class accomodates the two graph
        traversing algorithm BFS and DFS'''
    def __init__(self, graph) -> None:
        self.graph = graph
        self.visited = set()

    def BFS(self, node):
        '''BFS - performs Breadth First Search'''
        visited_bfs = []
        queue_bfs = []  
        visited_bfs.append(node) #holds visited nodes
        queue_bfs.append(node) #holds current node

        while queue_bfs:
            s = queue_bfs.pop() #pop the first node
            print (s, end = " ") #print the popped node

            #for all the neighbours of a node if
            #not visited, visit one by one and add them
            #one by one to the queue
            for neighbour in self.graph[s]:
                if neighbour not in visited_bfs:
                    visited_bfs.append(neighbour)
                    queue_bfs.append(neighbour)

    #using recursive DFS
    def DFS(self, node):
        '''DFS - performs Depth First Search which
        uses stack to print top of stack as the 
        current node'''
        if node not in self.visited:
            print(node, end=' ')
            self.visited.add(node)
            for neighbour in self.graph[node]:
                self.DFS(neighbour)


#DRIVER CODE
#graph with 7 nodes and "directed" edges        
graph = Graph(7)

#adding directed edges(source, destination)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 1)
graph.add_edge(2, 4)
graph.add_edge(3, 5)
graph.add_edge(5, 7)
graph.add_edge(6, 4)
graph.add_edge(3, 6)
graph.add_edge(7, 3)
print("The graph:",graph.getGraph())

traverse_graph = GraphTraversal(graph.getGraph())

print("Path using BFS:", end = ' ')
traverse_graph.BFS(1)
print()
print("Path using DFS:", end = ' ')
traverse_graph.DFS(1)