### check the next  item and  swap if its bigger


def bubbleSort(inp):
    for i in range(len(inp) - 1, 0, -1):
        for j in range(i):
            if inp[j] > inp[j + 1]:
                temp = inp[j]
                print(temp)
                inp[j] = inp[j + 1]
                inp[j + 1] = temp


inp = [1, 5, 2, 6, 9, 4]

bubbleSort(inp)
print(inp)

