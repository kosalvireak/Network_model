list_node = [0,1,2,3,4,5]
print("list_node",list_node)
# node and its network
list_network = []
# value of node by index
list_weight = []
# store value to node
list3={}

# create a value in and value out for comparison
i = 0


def add_edge(node1, node2, weight):
    global i
    node = node1, node2
    list_network.insert(i, node)
    list_weight.insert(i, weight)
    # list.insert(i,node2)
    i += 1


add_edge(0, 1, 6)
add_edge(0, 2, 4)
add_edge(1, 3, 3)
add_edge(1, 4, 2)
add_edge(2, 3, 2)    
add_edge(2, 4, 5)
add_edge(3, 5, 6)
add_edge(4, 5, 4)

print("list_network",list_network)
print("list_weight",list_weight)
for a in range(0, len(list_network)):
                if list_network[a][0] == 0:

                        #print(list_network[a], "= " , list_weight[a])
                        list3[list_network[a][1]] = list_weight[a]
                                
print(list3)
print("----------")














# i = 0
# while i < 7:
#         i += 1
        #print(list_network)
        #[(0, 1), (0, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 5), (4, 5)] 
        # if list_network[i][0] == :
        #         print(list_network[i][1])
        # # end start node
        # # begin normal node
        # no = 0
        # node4 = 0
        # min = 99999
        # for a in range(0, len(list_network)):
        #                 # we choose the send node 
        #                 if list_network[a][1] == i:
        #                         # print node list and its value
        #                         print(list_network[a], "= " , list_weight[a])
        #                         if list_weight[a] < min:
        #                                 min = list_weight[a]
                                
        #                         print(list_network[a][1]," = ",min)
        #                         # add receive node and its value to list 3
        #                         # no += list_weight[a]
        #                         list3[list_network[a][1]] = list_weight[a]
                                

                                
                                
        

                        
