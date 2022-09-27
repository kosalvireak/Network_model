# node and its network + weight
Network = []
# store new value to node
success_dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
# all node
Node = []
# weight
list_of_weight = []
# receive node
Receive_node = 5


def add_edge(node1, node2, weight):
    node = node1, node2, weight
    # add node and its network
    Network.append(node)
    # we don't include start node which is node 0
    if node1 != 0:
        if node1 not in Node:
            Node.append(node1)


add_edge(0, 1, 6)
add_edge(0, 2, 4)
add_edge(1, 3, 3)
add_edge(1, 4, 2)
add_edge(2, 3, 2)
add_edge(2, 4, 5)
add_edge(3, 5, 6)
add_edge(4, 5, 4)


# --> a code to auto add key from above function to success_dic EX: 1:0, 2:0


print("Node", Node)
print("Network", Network)

# Assign value to node that receive from node0
for i in range(len(Network)):
    if Network[i][0] == 0:
        # get its node
        new_node = Network[i][1]
        # get its weight
        new_value = Network[i][2]
        success_dic[new_node] = new_value
print("success_dic", success_dic)


for m in Node:
    print("------------")
    print(m)
    print("------------")
    temp_list = []
    for i in range(len(Network)):
        # Assign Network to temp list
        if Network[i][0] == m:
            node = Network[i][0], Network[i][1], Network[i][2]
            temp_list.append(node)

    print("temp_list", temp_list)

    if len(temp_list) == 2:
        # Compare 3rd elements of both
        
        if temp_list[0][2] < temp_list[1][2]:
            smallest = temp_list[0][2]
            smallest_key = temp_list[0][1]
            biggest = temp_list[1][2]
            biggest_key = temp_list[1][1]
        elif temp_list[1][2] < temp_list[0][2]:
            smallest = temp_list[1][2]
            smallest_key = temp_list[1][1]
            biggest = temp_list[0][2]
            biggest_key = temp_list[0][1]

        # assign smallest to success_dic
        success_dic[smallest_key] += smallest
        success_dic[temp_list[0][0]] = success_dic[temp_list[0][0]] - smallest

        # Compare its weight and the value of nod (1,3,3) weight is 3 and value of nod is 4
        if biggest < success_dic[temp_list[0][0]]:
            success_dic[biggest_key] += biggest
            success_dic[temp_list[0][0]
                        ] = success_dic[temp_list[0][0]] - biggest
        elif biggest > success_dic[temp_list[0][0]]:
            success_dic[biggest_key] += success_dic[temp_list[0][0]]

            success_dic[temp_list[0][0]] -= success_dic[temp_list[0][0]]
        # clear temp_list
        temp_list.clear()
    print(success_dic)

    if len(temp_list) == 1:

        if temp_list[0][2] >= success_dic[temp_list[0][0]]:
            success_dic[temp_list[0][1]] += success_dic[temp_list[0][0]]
        elif temp_list[0][2] <= success_dic[temp_list[0][0]]:
            success_dic[temp_list[0][1]] += temp_list[0][2]


print("============")
print(success_dic[Receive_node])
