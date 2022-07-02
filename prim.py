# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/minimum-spanning-trees-prims-algorithm/#whatisaminimumspanningtree

#create a class name Graph
class Graph: 
    #this is constructor
    def __init__(self, num_of_nodes): 
        self.m_num_of_nodes = num_of_nodes
        # create an empty adjacecy matrix with the nodes of 9 and all value equal to 0
        self.m_graph = [[0 for column in range(num_of_nodes)] 
                    for row in range(num_of_nodes)]
    #this is method ,used to reduce the number of edge, 
    def add_edge(self, node1, node2, weight): 
        self.m_graph[node1][node2] = weight # A to B = 4
        self.m_graph[node2][node1] = weight # B to A = 4 
        
      
            
      
    #this is method
    def prims_mst(self):
        # we create a large number, so that edge alwasy lesser when compare
        # flaot('inf') is mean to set the value to infinitive
        postitive_inf = float('inf')

        # we use this to check whether nodes are chosen or not
        selected_nodes = [False for node in range(self.m_num_of_nodes)]

        # we store our MST result here
        result = [[0 for column in range(self.m_num_of_nodes)] 
                    for row in range(self.m_num_of_nodes)]
        # print the graph out
        indx = 0
        for i in range(self.m_num_of_nodes):
            print(self.m_graph[i])
        # print False 
        print(selected_nodes)
       

        # while loop check the nodes that haven't choose
        while(False in selected_nodes):
            # assign the biggest value to minimum
            minimum = postitive_inf

            # The starting node
            start = 0

            # The ending node
            end = 0

            for i in range(self.m_num_of_nodes):
                
                if selected_nodes[i]:
                    for j in range(self.m_num_of_nodes):
                        # If the analyzed node have a path to the ending node AND its not included in the MST (to avoid cycles)
                        if (not selected_nodes[j] and self.m_graph[i][j]>0):  
                            # If the weight path analized is less than the minimum of the MST
                            if self.m_graph[i][j] < minimum:
                                # Defines the new minimum weight, the starting vertex and the ending vertex
                                minimum = self.m_graph[i][j]
                                start, end = i, j
   
            # Since we added the ending vertex to the MST, it's already selected:
            selected_nodes[end] = True

            # Filling the MST Adjacency Matrix fields:
            result[start][end] = minimum
            
            if minimum == postitive_inf:
                result[start][end] = 0

            #print("(%d.) %d - %d: %d" % (indx, start, end, result[start][end]))
            indx += 1
            
            result[end][start] = result[start][end]

        # Print the resulting MST
        # for node1, node2, weight in result:
        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))       
                
                
                
                
                
                # Example graph has 9 nodes
example_graph = Graph(9)
                
example_graph.add_edge(0, 1, 4)
example_graph.add_edge(1, 0, 4)
example_graph.add_edge(0, 2, 7)
example_graph.add_edge(1, 2, 11)
example_graph.add_edge(1, 3, 9)
example_graph.add_edge(1, 5, 20)
example_graph.add_edge(2, 5, 1)
example_graph.add_edge(3, 6, 6)
example_graph.add_edge(3, 4, 2)
example_graph.add_edge(4, 6, 10)
example_graph.add_edge(4, 8, 15)
example_graph.add_edge(4, 7, 5)
example_graph.add_edge(4, 5, 1)
example_graph.add_edge(5, 7, 3)
example_graph.add_edge(6, 8, 5)
example_graph.add_edge(7, 8, 12)


example_graph.prims_mst()
