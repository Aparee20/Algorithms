def InsertionSort(arr):

    size=len(arr)-1

    for i in range(1,size):
        print(arr[i])

        key = arr[i];
        j =i-1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


inp = [9,1,8, 5, 2, 3, 0]

InsertionSort(inp)
print(inp)
