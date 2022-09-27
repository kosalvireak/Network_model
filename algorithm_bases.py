# node and its network + weight
Network = []
# store new value to node
success_dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
# all node
Node = []
# weight
list_of_weight = []


def add_edge(node1, node2, weight):
    node = node1, node2, weight
    # add node and its network
    Network.append(node)
    if node1 != 0:
        if node1 not in Node:
            Node.append(node1)
    list_of_weight.append(weight)


add_edge(0, 1, 6)
add_edge(0, 2, 4)
add_edge(1, 3, 3)
add_edge(1, 4, 2)
add_edge(2, 3, 2)
add_edge(2, 4, 5)
add_edge(3, 5, 6)
add_edge(4, 5, 4)


# auto add key from above function to success_dic

print("Node", Node)
print("Network", Network)
print("success_dic", success_dic)
print("------------")

# Assign value to node that receive from node0

for i in range(len(Network)):
    if Network[i][0] == 0:
        # get its node
        new_node = Network[i][1]
        # get its weight
        new_value = Network[i][2]
        success_dic[new_node] = new_value
print("success_dic", success_dic)
temp_list = []

for i in range(len(Network)):
    # Assign Network to temp list
    if Network[i][0] == 1:
        node = Network[i][0], Network[i][1], Network[i][2]
        temp_list.append(node)

    # This is for temp_dic if it equal = 2
    # Compare 3rd elements of both
    smallest = 100
    if temp_list[]
    # clear temp_list
    # temp_list.clear()
print(temp_list)
