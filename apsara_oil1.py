dic = {0: 0, 1: 2, 2: 2, 3: 0, 4: 0, 5: 14}
Receive_node = 5
for i in range(Receive_node):
    if dic[i] != 0:
        print("Pumping station",i, "Still has weight of", dic[i], "left")
print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
