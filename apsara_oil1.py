
# node and its network
list_network = []
# value of node by index
list_weight = []
# store value to node
success_dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
list0 = {}
list_list0 = []
list1 = {}
list_list1 = []
list2 = {}
list_list2 = []
list3 = {}
list_list3 = []
list4 = {}
list_list4 = []

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

print("list_network", list_network)
print("list_weight", list_weight)
for a in range(0, len(list_network)):
    if list_network[a][0] == 0:
        list_list0.insert(a, list_weight[a])
        # list_list0.insert([a][1],list_weight[a])

        #print(list_network[a], "= " , list_weight[a])
        list0[list_network[a][1]] = list_weight[a]

    elif list_network[a][0] == 1:

        list_list1.insert(a, list_weight[a])

        #print(list_network[a], "= " , list_weight[a])
        list1[list_network[a][1]] = list_weight[a]
    elif list_network[a][0] == 2:

        list_list2.insert(a, list_weight[a])

        #print(list_network[a], "= " , list_weight[a])
        list2[list_network[a][1]] = list_weight[a]
    elif list_network[a][0] == 3:

        list_list3.insert(a, list_weight[a])

        #print(list_network[a], "= " , list_weight[a])
        list3[list_network[a][1]] = list_weight[a]
    elif list_network[a][0] == 4:

        list_list4.insert(a, list_weight[a])

        #print(list_network[a], "= " , list_weight[a])
        list4[list_network[a][1]] = list_weight[a]
print("success_dic", success_dic)
print("list0", list0)
print("list_list0", list_list0)
print("list1", list1)
print("list2", list2)
# print("list3", list3)
# print("list4", list4)
print("----------")


a = success_dic[1] + 6
success_dic.update({1: a})
b = success_dic[2] + 4
success_dic.update({2: b})


if len(list_list1) == 2:
    smallest = 1000
    a0 = list_list1[0]
    a1 = list_list1[1]
    if smallest > a0:
        smallest = a0
    if smallest > a1:
        smallest = a1

    print(list_list1)
    print(smallest)

    if list(list1)[0] == smallest:
        print(list(list1)[0])
    elif list(list1)[1] == smallest:
        print(list(list1)[1])
c = success_dic[3] + smallest
success_dic.update({3: c})
print(success_dic)

# i = 0
# while i < 7:
#         i += 1
# print(list_network)
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

print("----------------")