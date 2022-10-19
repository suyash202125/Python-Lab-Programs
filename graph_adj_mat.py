class Graph:
    
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed

        # Initialize the adjacency matrix
        # Create a matrix with `num_of_nodes` rows and columns
        self.m_adj_matrix = [[0 for column in range(num_of_nodes+1)] 
                            for row in range(num_of_nodes+1)]

    #assigning weights
    def add_edge(self, node1, node2, weight):
        self.m_adj_matrix[node1][node2] = weight

        if not self.m_directed:
            self.m_adj_matrix[node2][node1] = weight

    #printing adjacency matrix
    def print_adj_matrix(self):
        print(self.m_adj_matrix)

#Driver Code
#graph with 3 nodes and undirected edges        
graph = Graph(3, False)

#adding edge between nodes and respective weights
graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 10)

#print the adjacency matrix
graph.print_adj_matrix()