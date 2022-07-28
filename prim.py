# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/minimum-spanning-trees-prims-algorithm/#whatisaminimumspanningtree

# create a class name Graph
class Graph:
    #this is constructor
    # In python we call init
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        # create an empty adjacency matrix with the nodes of 9 and all value equal to 0
        self.m_graph = [[0 for column in range(num_of_nodes)]
                        for row in range(num_of_nodes)]
    # this is method ,used to reduce the number of edge,

    def add_edge(self, node1, node2, weight):
        # array [line][colum]
        #i.e. m_graph [1][3] =5 /line 1 colum 3 = 5
        self.m_graph[node1][node2] = weight  # A to B = 4
        self.m_graph[node2][node1] = weight  # B to A = 4

    #this is method

    def prims_mst(self):
        # we create a large number, so that edge alway lesser when compare
        # float('inf') is mean to set the value to infinitive
        postitive_inf = float('inf')

        # we use this to check whether nodes are chosen or not
        # this line make all the node to False
        # 0 : False
        # 1 : False
        # 2 : False
        # 3 : False
        # 4 : False
        # 5 : False
        # 6 : False
        # 7 : False
        # 8 : False
        selected_nodes = [False for node in range(self.m_num_of_nodes)]

        # we store our MST result here
        result = [[0 for column in range(self.m_num_of_nodes)]
                  for row in range(self.m_num_of_nodes)]
        # print the graph out
        index = 0
        for i in range(self.m_num_of_nodes):
            print(self.m_graph[i])
        # print False
        print(selected_nodes)

        # Loop end when all the node aren't False
        while(False in selected_nodes):
            # assign the biggest value to minimum
            minimum = postitive_inf

            # The starting node
            start = 0

            # The ending node
            end = 0
            # loop run from 0 to 8 since m_num_of_nodes = 9
            for i in range(self.m_num_of_nodes):
                # if node has been select it will go into that loop
                #for the first try there is no selected node since it all false 
                # code will hop to the selected_nodes[end] = True to make a node true, end = 0 so node0 will become True
                if selected_nodes[i]: #second run code already True so it enter the loop
                    #we run j from 0 to , but this j loop stay under i loop so, i=0 and j start run from 0 >8
                    #this make sure that we go to all element⁡
                    for j in range(self.m_num_of_nodes):
                        # selected_node[0] = True// m_graph[0][0] = 0,by doing this we take only node that false cus not false oi true and we go into loop
                        # selected_node[1] = false, not sele = true // m_graph[0][1] = 4>0 --> go into loop
                        # selected_node[2] = false, not sele = true // m_graph[0][2] = 7>0 --> go into loop
                        # selected_node[3] & [4] = false, not sele = true // m_graph[0][3] & [0][4] = 0 
                        # selected_node[5] = false, not sele = true // m_graph[0][5] = 20>0 --> go into loop


                        if (not selected_nodes[j] and self.m_graph[i][j] > 0):
                            # m_graph [0][0] = 4 < minimum = inf
                            # m_graph [0][2] = 7 !< minimum = 4
                            # m_graph [0][5] = 20 !< minimum = 4
                            if self.m_graph[i][j] < minimum:
                                # change minimun to 4 which be long to m_graph[0][1]
                                minimum = self.m_graph[i][j]
                                #start 0, end 1
                                start, end = i, j

        
            selected_nodes[end] = True

            #assign the [0][0] to infinitive
            result[start][end] = minimum

            if minimum == postitive_inf:
                result[start][end] = 0

            #increase index
            index += 1

            result[end][start] = result[start][end]

        # Print the resulting MST
        # for node1, node2, weight in result:
        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))


                # Example graph has 9 nodes
# create a object example_graph from a Graph class
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
