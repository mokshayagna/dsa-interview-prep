arr = [3, 0, 1, 0, 4, 0, 2]
n = len(arr)
prefix_max = [0]*len(arr)
prefix_max[0] = arr[0]
for i in range(1,len(arr)):
    prefix_max[i] = max(arr[i],prefix_max[i-1])

suffix_max = [0]*len(arr)
suffix_max[n-1] = arr[n-1]
for i in range(n-2,-1,-1):
    suffix_max[i] = max(arr[i],suffix_max[i + 1])

total = 0
for i in range(0,len(arr)):
    total += min(prefix_max[i],suffix_max[i]) - arr[i]
print(total)