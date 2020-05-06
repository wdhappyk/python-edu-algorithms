def count(arr):
    return 1 + count(arr[1:]) if len(arr) else 0


print(count([]))
print(count([1, 2, 3]))
