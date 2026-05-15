arr = [1, -2, 1, 0, 5]
target = 0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i],arr[j])
print(False)