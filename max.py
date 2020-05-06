def max(arr):
    if len(arr) == 1:
        return arr[0]

    if len(arr) > 1:
        n = max(arr[1:])
        return arr[0] if arr[0] > n else n

    return 0


print(max([3, 100, 3]))
print(max([]))
