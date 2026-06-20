def first_last_occurrence(arr, target):
    # First occurrence
    l, r = 0, len(arr) - 1
    first = -1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            first = mid
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    # Last occurrence
    l, r = 0, len(arr) - 1
    last = -1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            last = mid
            l = mid + 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return (first, last)

arr = [1, 2, 5, 5, 5, 9]
print(first_last_occurrence(arr, 5))