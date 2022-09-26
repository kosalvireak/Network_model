# node and its network
list_of_network = []
# store new value to node
list_of_new_value = {}
# all node
nodes = []


def add_edge(node1, node2, weight):
    node = node1, node2, weight
    # add node and its network
    list_of_network.append(node)
    # list of all nodes
    if node1 not in nodes:
        nodes.append(node1)
    if node2 not in nodes:
        nodes.append(node2)
    # list.insert(i,node2)


add_edge(0, 1, 6)
add_edge(0, 2, 4)
add_edge(1, 3, 3)
add_edge(1, 4, 2)
add_edge(2, 3, 2)
add_edge(2, 4, 5)
add_edge(3, 5, 6)
add_edge(4, 5, 4)

print(nodes)
print(list_of_network)
print(list_of_weight)
print("------------")