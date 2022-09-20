
# node and its network
list1 = []
# value of node by index
list2 = []
# store value to node
list3={}

# create a value in and value out for comparison
i = 0


def add_edge(node1, node2, weight):
    global i
    node = node1, node2
    list1.insert(i, node)
    list2.insert(i, weight)
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

print(list1)
# print(list1[5])
print(list2)
first = 10
for a in range(0, len(list1)):
        #for b in range(0, len(list1)):
        #for b in range(0, 2):
        
                if list1[a][0] == 0:
                        # print node list and its value
                        print(list1[a], "= " , list2[a])
                        
                        # assign the end node and the value to dictionary
                        list3[list1[a][1]] = list2[a]
                                
print(list3)
print("----------")
i = 0
while i < 7:
        i += 1
        #print(list1)
        #[(0, 1), (0, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 5), (4, 5)] 
        if list1[i][0] == :
                print(list1[i][1])
        # # end start node
        # # begin normal node
        # no = 0
        # node4 = 0
        # min = 99999
        # for a in range(0, len(list1)):
        #                 # we choose the send node 
        #                 if list1[a][1] == i:
        #                         # print node list and its value
        #                         print(list1[a], "= " , list2[a])
        #                         if list2[a] < min:
        #                                 min = list2[a]
                                
        #                         print(list1[a][1]," = ",min)
        #                         # add receive node and its value to list 3
        #                         # no += list2[a]
        #                         list3[list1[a][1]] = list2[a]
                                

                                
                                
        

                        
