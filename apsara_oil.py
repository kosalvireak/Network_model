# node and its network
list_of_network = []
# value of node by index
list_of_weight = []
# store new value to node
list_of_new_value = {}
# all node
nodes = []


def add_edge(node1, node2, weight):
    node = node1, node2
    # add node and its network
    list_of_network.append(node)
    # create a weight list the value correspond to list_of_network's index
    list_of_weight.append(weight)
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


# create a value in and value out for comparison
j = 0
while j <= (len(list_of_network)):
    for i in range (len(list_of_network)):
        # check the weight
        # i = 0 , (0,1) = 5 add value 5 to key 1 in list_of_new_value

        if list_of_network[i][0] == j:
            list_of_new_value[list_of_network[i][1]] = list_of_weight[i]
    j = j + 1 

#print(list_of_new_value)

#check all the network រកទីតាំងដើម ដើម្បីផ្តល់តម្លៃទៅទីតាំងបញ្ចប់
list_of_new={}
for nod in nodes:
    for i in range (len(list_of_network)):
        if list_of_network[i][0] == nod:
            list_of_new[list_of_network[i][1]] = list_of_weight[i]
print('old list',list_of_new)


for nod in nodes:
    temp_list ={}
    out1 = 0
    out2 = 0
    max = 500
    min = 100
    for i in range (len(list_of_network)):
        if list_of_network[i][0] == nod: ### send node will change to nod
            out1 = list_of_network[i][1]
            out2 = list_of_weight[i]
            if out2 < max:
                max = out2
            temp_list[out1] = out2
    i = 0
    key = 0
    key2 =0
    while i < len(temp_list):
        first_value = list(temp_list.values())[i]
        if first_value < min:
            min = first_value
            key = i
        else: 
            key2 = i
        i += 1
        
    #small = temp_list[key]
    # # get key of temp list by its index
    # keys_list = list(temp_list)
    # keys = keys_list[key]
    # list_of_new.update({keys:min})
    
    
# # reduce send node by what has been sent
#     list_of_new.update({nod:3}) 
#     key2 = keys_list[key2]
#     list_of_new.update({key2:min})

print('new list',list_of_new)    
print("key",key)
print("----------------------------")
print('temp list',temp_list)
print("----------------------------")
print("min",min)

# i = 0
# while i < len(temp_list):
#     first_value = list(temp_list.values())[i]
#     if first_value < min:
#         min = first_value
#     i += 1
# print(min)
    