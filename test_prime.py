# num_of_nodes = 9
# m_num_of_nodes = num_of_nodes
# m_graph = [[0 for column in range(num_of_nodes)] for row in range (num_of_nodes)]

# for i in range(num_of_nodes):
#         print(m_graph[i])


# print(m_graph[2][2])
# i = 0
# selected_nodes = [False for node in range(num_of_nodes)]
# for i in range(m_num_of_nodes):
#     print(selected_nodes)
#     if not selected_nodes[i]:
#         print(m_num_of_nodes,[i],selected_nodes)

# print(selected_nodes)
# result = [[0 for column in range(m_num_of_nodes)] 
#                     for row in range(m_num_of_nodes)]
# print(result)

# for i in range(9):
#         print(i,": False")
#     for j in range(0+i, 9):
#         print(i,j)
#        0  1  2  3  4  5  6  7  8
list = [[0, 4, 7, 0, 0, 0, 0, 0, 0],    #0
        [4, 0, 11, 9, 0, 20, 0, 0, 0],  #1
        [7, 11, 0, 0, 0, 1, 0, 0, 0],   #2
        [0, 9, 0, 0, 2, 0, 6, 0, 0],    #3
        [0, 0, 0, 2, 0, 1, 10, 5, 15],  #4
        [0, 20, 1, 0, 1, 0, 0, 3, 0],   #5
        [0, 0, 0, 6, 10, 0, 0, 0, 5],   #6
        [0, 0, 0, 0, 5, 3, 0, 0, 12],   #7
        [0, 0, 0, 0, 15, 0, 5, 12, 0]]  #8
