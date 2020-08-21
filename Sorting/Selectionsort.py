# set a min pos and in every iteration find the min pos  value so  swapping

def Selectionsort(inp):
    for i in range(0,len(inp)-1):
        minpos =i

        for j in range(i,len(inp)):
            minpos =j


            if inp[j] > inp[j + 1]:
                temp = inp[j]
                inp[j] = inp[j + 1]
                inp[j + 1] = temp


inp = [1, 5, 2, 6, 9, 4]

Selectionsort(inp)
print(inp)


