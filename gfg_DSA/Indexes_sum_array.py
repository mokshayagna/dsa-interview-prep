arr= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 15
l = 0
total = 0
ans = []
for r in range(len(arr)):
    total = total + arr[r]
    while(total > target):
        total = total - arr[l]
        l = l+1
    if target == total:
        ans.append(l+1)
        ans.append(r+1)
        break
print(ans)
        