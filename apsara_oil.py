# node and its network
list_of_network = []
# value of node by index
list_of_weight = []
# store value to node
list3={}

# create a value in and value out for comparison
i = 0


def add_edge(node1, node2, weight):
    global i
    node = node1, node2
    list_of_network.insert(i, node)
    list_of_weight.insert(i, weight)
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

print(list_of_network)
print(list_of_weight)
