arr = [1, -2, 1, 0, 5]
target = 2


# brute force
"""
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i],arr[j])
print(False)
"""
# efficient approach
i = 0
j = len(arr) - 1
arr.sort()
while i < j:
    if arr[i] + arr[j] > target:
        j -= 1
    elif arr[i] + arr[j] < target:
        i += 1
    else:
        print(arr[i], arr[j])
        break