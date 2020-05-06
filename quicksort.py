def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([1, 5, 6, 10, 12, 0, -100, 19, 1, 1, 1]))
