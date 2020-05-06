def insertion_sort(arr):
    for i in range(1, len(arr) - 1):
        x = arr[i]
        j = i
        while j > 0 and arr[j - 1] > x:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = x

        print(arr)


insertion_sort([2, 1, 1, 7, 1, 12])
