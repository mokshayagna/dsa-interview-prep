arr = [12, 35, 1, 10, 34, 1]

largest = -1
second_largest = -1

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

for i in range(len(arr)):
    if arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]
print(second_largest)